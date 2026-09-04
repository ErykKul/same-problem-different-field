#!/usr/bin/env python3
"""Rebuild the five non-redistributable abstract files listed in data/restricted.csv.

The bundle ships abstracts only where a license covers them (arXiv descriptive metadata is CC0 per
arXiv's API terms; a PMC subset is CC BY, attributed in the manifest). Five papers have no such
license (two publisher pages, one IEEE, and two PMC NC/ND entries handled conservatively), so only
their ids, source URLs, and sha256 checksums ship; this script re-fetches each abstract from its
publisher page and rebuilds `data/md/<id>.md`. The checksums verify whether the rebuilt file matches
the frozen bytes the paper's numbers were computed from; on drift or fetch failure the frozen files
are available from the author for verification.

Run:  python src/fetch_restricted.py        (network; writes only files that are missing)
      python src/fetch_restricted.py --force
"""
import csv, hashlib, html, os, re, sys

import requests

RESTRICTED = "data/restricted.csv"
H = {"User-Agent": "same-problem-different-field repro (mailto:eryk.kulikowski@kuleuven.be)"}


def meta(page, *names):
    for n in names:
        m = re.search(r'<meta[^>]+(?:name|property)=["\']%s["\'][^>]+content=["\'](.*?)["\']' % re.escape(n),
                      page, re.I | re.S) or \
            re.search(r'<meta[^>]+content=["\'](.*?)["\'][^>]+(?:name|property)=["\']%s["\']' % re.escape(n),
                      page, re.I | re.S)
        if m:
            return html.unescape(m.group(1)).strip()
    return None


def fetch_md(url):
    r = requests.get(url, headers=H, timeout=60, allow_redirects=True)
    r.raise_for_status()
    page = r.text
    title = meta(page, "citation_title", "og:title", "dc.Title")
    abstract = meta(page, "citation_abstract", "dc.Description") or meta(page, "og:description")
    if abstract and len(abstract) < 300:  # publisher meta is often a truncated teaser; a real
        abstract = None                   # abstract is longer -> let the OpenAlex fallback handle it
    if not (title and abstract):
        return None
    return f"# {title}\n\n## Abstract\n\n{abstract}\n"


def fetch_md_openalex(doi):
    """Fallback: rebuild from OpenAlex's CC0 record (abstract_inverted_index reconstruction).
    The text will differ from the frozen publisher scrape (the checksum reports that), but the
    corpus stays complete and reproduce.py can run."""
    r = requests.get(f"https://api.openalex.org/works/doi:{doi}",
                     params={"select": "title,abstract_inverted_index"}, headers=H, timeout=60)
    r.raise_for_status()
    j = r.json()
    inv = j.get("abstract_inverted_index")
    if not (j.get("title") and inv):
        return None
    pos = {}
    for w, idxs in inv.items():
        for i in idxs:
            pos[i] = w
    abstract = " ".join(pos[i] for i in sorted(pos))
    return f"# {j['title']}\n\n## Abstract\n\n{abstract}\n"


def main():
    force = "--force" in sys.argv
    rows = list(csv.DictReader(open(RESTRICTED)))
    ok = drift = missing = present = 0
    for r in rows:
        path = f"data/md/{r['id']}.md"
        if os.path.exists(path) and not force:
            got = hashlib.sha256(open(path, "rb").read()).hexdigest()
            present += 1
            print(f"[restricted] {r['id']}: present, "
                  f"{'matches the frozen sha256' if got == r['md_sha256'] else 'sha256 DIFFERS from frozen'}")
            continue
        try:
            md = fetch_md(r["source_url"])
        except requests.RequestException as e:
            md = None
            print(f"[restricted] {r['id']}: publisher fetch failed ({type(e).__name__})", file=sys.stderr)
        via = "publisher page"
        if not md and r.get("doi"):
            try:
                md = fetch_md_openalex(r["doi"])
                via = "OpenAlex record (fallback)"
            except requests.RequestException as e:
                print(f"[restricted] {r['id']}: OpenAlex fallback failed ({type(e).__name__})",
                      file=sys.stderr)
        if not md:
            missing += 1
            print(f"[restricted] {r['id']}: could not rebuild from {r['source_url']}", file=sys.stderr)
            continue
        open(path, "w", encoding="utf-8").write(md)
        got = hashlib.sha256(md.encode("utf-8")).hexdigest()
        if got == r["md_sha256"]:
            ok += 1
            print(f"[restricted] {r['id']}: rebuilt from {via}, matches the frozen sha256")
        else:
            drift += 1
            print(f"[restricted] {r['id']}: rebuilt from {via}, but DIFFERS from the frozen bytes "
                  f"(page changed or scrape format differs); numbers may shift slightly. "
                  f"The frozen file is available for verification (see README).")
    print(f"[restricted] done: {present} present, {ok} rebuilt exact, {drift} rebuilt with drift, "
          f"{missing} not rebuilt.")
    if missing:
        sys.exit(1)


if __name__ == "__main__":
    main()
