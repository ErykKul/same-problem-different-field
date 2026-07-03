"""Raw downloaded file -> clean Markdown.

PDF via PyMuPDF (self-contained, no system poppler needed); generic HTML via
markdownify. arXiv HTML has a dedicated, higher-fidelity path in
arxiv_lib.html_to_md (LaTeXML structure + math kept as LaTeX).

Faithfulness note: PyMuPDF gives reading-order text and loses most display math.
That is acceptable for the probe (we feed prose + symbols to the distiller). The
fidelity upgrade is GROBID/Docling (structured TEI): a drop-in for pdf_to_md.
"""
from __future__ import annotations
import re
import unicodedata
import fitz  # PyMuPDF
from bs4 import BeautifulSoup
from markdownify import markdownify as _md

_REF_HEAD = re.compile(r"(?im)^\s*(references|bibliography|acknowledge?ments?)\s*$")


def _dehyphenate(text: str) -> str:
    return re.sub(r"(\w)-\n(\w)", r"\1\2", text)


def _trim_refs(text: str) -> str:
    hits = list(_REF_HEAD.finditer(text))
    return text[:hits[-1].start()].rstrip() if hits else text


def pdf_to_md(path: str) -> tuple[str, str]:
    doc = fitz.open(path)
    title = (doc.metadata or {}).get("title") or ""
    pages = [page.get_text("text") for page in doc]
    doc.close()
    text = unicodedata.normalize("NFKC", "\n".join(pages))  # ﬁ->fi, ﬂ->fl, etc.
    text = _dehyphenate(text)
    text = re.sub(r"[ \t]+\n", "\n", text)
    text = re.sub(r"\n{3,}", "\n\n", text)
    text = _trim_refs(text)
    if not title:
        for line in text.splitlines():
            if len(line.strip()) > 12:
                title = line.strip()
                break
    return title.strip(), text.strip()


def html_to_md(html: str) -> tuple[str, str]:
    soup = BeautifulSoup(html, "lxml")
    for sel in ("script", "style", "nav", "header", "footer", "form", "noscript"):
        for t in soup.select(sel):
            t.decompose()
    main = soup.select_one("main, article, #content, .content") or soup.body or soup
    title = soup.title.get_text(strip=True) if soup.title else ""
    body = _md(str(main), heading_style="ATX", strip=["a"]).strip()
    body = re.sub(r"\n{3,}", "\n\n", body)
    return title, _trim_refs(body)
