"""arXiv fetch + normalize-to-Markdown helpers for the probe.

Two jobs:
  1. search(query, ...)        -> candidate papers (for curation)
  2. fetch_paper(arxiv_id)     -> clean Markdown (abstract + body), math kept as LaTeX

No pandoc needed: arXiv serves LaTeXML HTML at arxiv.org/html/<id> (recent) or
ar5iv (older). We strip that HTML to faithful Markdown, replacing <math> nodes
with their original LaTeX (the `alttext` LaTeXML stores) so the math survives.
"""
from __future__ import annotations
import re, sys, time, html as _html
import xml.etree.ElementTree as ET
import requests
from bs4 import BeautifulSoup, NavigableString
from markdownify import markdownify as _md

UA = {"User-Agent": "same-problem-different-field/1.0 (research; https://github.com/ErykKul/same-problem-different-field)"}
API = "http://export.arxiv.org/api/query"
ATOM = "{http://www.w3.org/2005/Atom}"
ARX = "{http://arxiv.org/schemas/atom}"

# section titles we never want in the distillation input
SKIP_SECTION = re.compile(
    r"\b(references?|bibliography|acknowledg|appendix|funding|"
    r"author contribution|conflict|supplementary|data availability)\b", re.I)


def _norm_id(arxiv_id: str) -> str:
    """Accept '2401.18059', 'arXiv:2401.18059v2', full URLs, and old-style ids
    ('cond-mat/0501639') -> bare id (no version). Old-style ids keep their
    archive prefix (it is part of the id), new-style ids do not."""
    s = arxiv_id.strip()
    m = re.search(r"arxiv\.org/(?:abs|pdf|html)/(.+)$", s, re.I)
    if m:
        s = m.group(1)
    s = re.sub(r"^arxiv:", "", s, flags=re.I)
    s = re.sub(r"v\d+$", "", s.rstrip("/"))
    return s


# ---------------------------------------------------------------- search
def _get(params: dict, timeout: int = 30, retries: int = 4) -> str:
    """GET the arXiv API with backoff on 429 / transient errors (the API asks
    for a few seconds between calls)."""
    delay = 3.0
    for attempt in range(retries):
        try:
            r = requests.get(API, params=params, headers=UA, timeout=timeout)
            if r.status_code == 429:
                raise requests.HTTPError("429 rate limited", response=r)
            r.raise_for_status()
            return r.text
        except (requests.HTTPError, requests.ConnectionError, requests.Timeout):
            if attempt == retries - 1:
                raise
            time.sleep(delay)
            delay *= 2
    raise RuntimeError("unreachable")


def search(query: str, category: str | None = None, max_results: int = 8,
           sort: str = "relevance") -> list[dict]:
    q = query
    if category:
        q = f"cat:{category} AND ({query})"
    params = {"search_query": q, "start": 0, "max_results": max_results,
              "sortBy": "relevance" if sort == "relevance" else "submittedDate",
              "sortOrder": "descending"}
    root = ET.fromstring(_get(params))
    out = []
    for e in root.findall(f"{ATOM}entry"):
        idu = e.findtext(f"{ATOM}id") or ""
        prim = e.find(f"{ARX}primary_category")
        out.append({
            "id": _norm_id(idu),
            "title": " ".join((e.findtext(f"{ATOM}title") or "").split()),
            "primary_category": prim.get("term") if prim is not None else "",
            "published": (e.findtext(f"{ATOM}published") or "")[:10],
            "summary": " ".join((e.findtext(f"{ATOM}summary") or "").split()),
        })
    return out


def fetch_meta(arxiv_id: str) -> dict:
    arxiv_id = _norm_id(arxiv_id)
    root = ET.fromstring(_get({"id_list": arxiv_id}))
    e = root.find(f"{ATOM}entry")
    if e is None:
        raise RuntimeError(f"no metadata for {arxiv_id}")
    prim = e.find(f"{ARX}primary_category")
    doi = e.findtext(f"{ARX}doi")
    return {
        "id": arxiv_id,
        "title": " ".join((e.findtext(f"{ATOM}title") or "").split()),
        "authors": [a.findtext(f"{ATOM}name") for a in e.findall(f"{ATOM}author")],
        "primary_category": prim.get("term") if prim is not None else "",
        "published": (e.findtext(f"{ATOM}published") or "")[:10],
        "doi": doi,
        "abstract": " ".join((e.findtext(f"{ATOM}summary") or "").split()),
    }


# ---------------------------------------------------------------- html -> md
def _is_latexml(text: str) -> bool:
    """True only for a real LaTeXML full-text page. Rejects the arXiv abstract
    landing page (which 'arxiv.org/html/<id>' serves when no HTML exists) - it
    has no ltx_ article structure, only nav chrome."""
    return ("ltx_abstract" in text or 'class="ltx_section"' in text
            or text.lower().count("<math") >= 3)


def _get_html(arxiv_id: str) -> tuple[str, str] | tuple[None, None]:
    arxiv_id = _norm_id(arxiv_id)
    for url in (f"https://arxiv.org/html/{arxiv_id}",
                f"https://ar5iv.org/html/{arxiv_id}",
                f"https://ar5iv.labs.arxiv.org/html/{arxiv_id}"):
        try:
            r = requests.get(url, headers=UA, timeout=30, allow_redirects=True)
        except requests.RequestException:
            continue
        if r.status_code == 200 and _is_latexml(r.text):
            return r.text, r.url
    return None, None


def _inline_math(soup: BeautifulSoup) -> None:
    """Replace every <math> with its LaTeX (alttext), so it survives markdownify."""
    for m in soup.find_all("math"):
        alt = m.get("alttext") or m.get("alttext".upper()) or ""
        alt = _html.unescape(alt).strip()
        if not alt:
            alt = m.get_text(" ", strip=True)
        display = (m.get("display") == "block")
        m.replace_with(NavigableString(f"\n$$ {alt} $$\n" if display else f" ${alt}$ "))


def _clean(soup: BeautifulSoup) -> None:
    for sel in ["script", "style", "figure", "img", "svg",
                ".ltx_bibliography", ".ltx_pagination", ".ltx_role_footnote",
                ".ar5iv-footer", ".ltx_authors", ".ltx_dates"]:
        for t in soup.select(sel):
            t.decompose()
    # citation markers -> drop (keep prose readable)
    for c in soup.select("cite, .ltx_cite"):
        c.decompose()


def html_to_md(html: str) -> tuple[str, str]:
    soup = BeautifulSoup(html, "lxml")
    _inline_math(soup)
    _clean(soup)

    title_el = soup.select_one("h1.ltx_title, h1.ltx_title_document, .ltx_title_document")
    title = title_el.get_text(" ", strip=True) if title_el else ""

    parts = []
    abs = soup.select_one(".ltx_abstract")
    if abs:
        atxt = abs.get_text(" ", strip=True)
        atxt = re.sub(r"^\s*abstract\s*", "", atxt, flags=re.I)
        parts.append("## Abstract\n\n" + atxt)

    sections = soup.select("section.ltx_section")
    if sections:
        for sec in sections:
            head = sec.select_one("h2, h3, .ltx_title_section")
            htitle = head.get_text(" ", strip=True) if head else ""
            if htitle and SKIP_SECTION.search(htitle):
                continue
            body_md = _md(str(sec), heading_style="ATX", strip=["a"]).strip()
            body_md = re.sub(r"\n{3,}", "\n\n", body_md)
            if body_md:
                parts.append(body_md)
    else:  # fallback: whole main body
        main = soup.select_one("article, .ltx_page_main, body")
        if main:
            parts.append(re.sub(r"\n{3,}", "\n\n",
                                _md(str(main), heading_style="ATX", strip=["a"]).strip()))

    body = "\n\n".join(parts)
    body = re.sub(r"[ \t]+\n", "\n", body)
    return title, body


def fetch_paper(arxiv_id: str) -> dict:
    """Return {meta..., 'markdown': str, 'fulltext': bool, 'source_url': str}."""
    meta = fetch_meta(arxiv_id)
    html, src = _get_html(arxiv_id)
    if html:
        t, body = html_to_md(html)
        meta["title"] = meta["title"] or t
        meta["markdown"] = body
        meta["fulltext"] = True
        meta["source_url"] = src
    else:  # metadata-only fallback (abstract only)
        meta["markdown"] = "## Abstract\n\n" + meta["abstract"]
        meta["fulltext"] = False
        meta["source_url"] = f"https://arxiv.org/abs/{meta['id']}"
    return meta


if __name__ == "__main__":
    # quick CLI: python arxiv_lib.py search "<query>" [category]
    #            python arxiv_lib.py fetch <id>
    cmd = sys.argv[1] if len(sys.argv) > 1 else "search"
    if cmd == "search":
        cat = sys.argv[3] if len(sys.argv) > 3 else None
        for p in search(sys.argv[2], category=cat, max_results=8):
            print(f"{p['id']:18} [{p['primary_category']:12}] {p['published']}  {p['title']}")
    elif cmd == "fetch":
        p = fetch_paper(sys.argv[2])
        print(f"# {p['title']}\nfulltext={p['fulltext']} src={p['source_url']} "
              f"chars={len(p['markdown'])}\n")
        print(p["markdown"][:1500])
