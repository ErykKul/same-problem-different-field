"""Download an open URL to disk with provenance (sha256, type, status).

Source-agnostic: an open-access publisher PDF or any directly fetchable URL.
arXiv links are handled upstream by arxiv_lib (higher fidelity), so they do not
normally reach here.
"""
from __future__ import annotations
import hashlib
from pathlib import Path
import requests

BROWSER_UA = {
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 "
                  "(KHTML, like Gecko) Chrome/124.0 Safari/537.36",
    "Accept": "application/pdf,text/html,*/*",
}


def _ext_for(content_type: str, head: bytes) -> str:
    ct = (content_type or "").lower()
    low = head[:512].lower()
    if head[:4] == b"%PDF" or "pdf" in ct:
        return "pdf"
    if "html" in ct or b"<!doctype html" in low or b"<html" in low:
        return "html"
    if "xml" in ct:
        return "xml"
    return "bin"


def download(url: str, dest_dir: str | Path, stem: str, timeout: int = 60) -> dict:
    dest_dir = Path(dest_dir)
    dest_dir.mkdir(parents=True, exist_ok=True)
    r = requests.get(url, headers=BROWSER_UA, timeout=timeout, allow_redirects=True)
    r.raise_for_status()
    content = r.content
    ctype = r.headers.get("Content-Type", "").split(";")[0].strip()
    ext = _ext_for(ctype, content[:512])
    path = dest_dir / f"{stem}.{ext}"
    path.write_bytes(content)
    return {
        "path": str(path),
        "ext": ext,
        "bytes": len(content),
        "sha256": hashlib.sha256(content).hexdigest(),
        "content_type": ctype,
        "http_status": r.status_code,
        "final_url": r.url,
    }


if __name__ == "__main__":
    import sys, json
    print(json.dumps(download(sys.argv[1], "data/raw",
                              sys.argv[2] if len(sys.argv) > 2 else "dl"), indent=2))
