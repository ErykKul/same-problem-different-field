#!/usr/bin/env python3
"""Build a Markdown corpus from a CSV of paper links.

Each input row points at one paper (an arXiv link/id, or any openly fetchable
PDF / HTML URL). The script fetches it, normalizes to Markdown with YAML
front-matter, and records provenance in data/manifest.jsonl.

This is the PUBLIC build: it pulls only arXiv and open URLs. A row whose URL is a
paywalled / non-arXiv resolver (e.g. a bare doi.org link with no open copy) needs
institutional access; the public build SKIPS it with a clear message and keeps
going. The headline result still holds on the open subset.

CSV columns (all optional except `url`; label columns are copied verbatim):
    id            short stable slug (auto-generated from family+field if blank)
    url           arXiv link/id, or an open PDF / HTML URL
    family        structural-family key (Mode A): members share the same math core
    field         domain / discipline
    role          member | distractor
    method_named  yes | no | ?   (does the paper name the method; for the cheat analysis)
    license       OA license if known (governs redistribution of derived md)
    note          free text
Lines beginning with '#' are treated as comments. Re-running skips papers whose
Markdown already exists (use --force to rebuild).

Usage:
    python src/build_dataset.py datasets/mode_a_seed_families.csv --out data
"""
from __future__ import annotations
import argparse, csv, hashlib, io, json, re, sys, time
from datetime import datetime, timezone
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import fetch, convert, arxiv_lib  # noqa: E402

ARXIV_URL = re.compile(r"arxiv\.org/(?:abs|pdf|html)/([\w.\-/]+?)(?:v\d+)?/?$", re.I)
ARXIV_BARE = re.compile(r"^(?:arxiv:)?(\d{4}\.\d{4,5}|[a-z\-]+(?:\.[A-Z]{2})?/\d{7})(?:v\d+)?$", re.I)
# DOI / institutional resolvers: a link that resolves to a publisher landing page,
# not an open full text. The public build cannot fetch these without institutional
# access, so it skips them (see _needs_institutional_access).
PAYWALL_HOSTS = ("doi.org", "dx.doi.org", "hdl.handle.net")
LABEL_COLS = ("family", "field", "role", "method_named", "license", "note")
FM_ORDER = ("id", "title", "source_type", "source_url", "fulltext", "sha256",
            "bytes", "retrieved_at", "md_chars", *LABEL_COLS)


def _slug(s: str) -> str:
    return re.sub(r"[^a-z0-9]+", "-", (s or "").lower()).strip("-")[:40]


def _auto_id(row: dict, n: int) -> str:
    base = "-".join(filter(None, (_slug(row.get("family", "")), _slug(row.get("field", "")))))
    return f"{base}-{n:03d}" if base else f"item-{n:03d}"


def _arxiv_id(url: str) -> str | None:
    url = url.strip()
    m = ARXIV_URL.search(url) or ARXIV_BARE.match(url)
    return m.group(1) if m else None


def _needs_institutional_access(url: str, row: dict) -> bool:
    """True if this row is a paywalled / non-arXiv resolver the public build cannot
    fetch openly. arXiv and local files are always fetchable, so they return False
    here. Otherwise we skip a bare DOI/handle resolver link, or any row the curator
    flagged as paywalled / needing institutional access (in license or note)."""
    url = (url or "").strip()
    if _arxiv_id(url):
        return False
    if url.startswith("file://") or Path(url).exists():
        return False
    host = re.sub(r"^[a-z]+://", "", url, flags=re.I).split("/", 1)[0].lower()
    host = host.split("@")[-1].split(":")[0]
    if host in PAYWALL_HOSTS:
        return True
    flag = (row.get("license", "") + " " + row.get("note", "")).lower()
    return any(w in flag for w in ("paywall", "institutional", "needs access", "no oa"))


def _yaml(v) -> str:
    if isinstance(v, bool):
        return "true" if v else "false"
    if isinstance(v, int):
        return str(v)
    return '"' + str(v).replace('"', "'").replace("\n", " ") + '"'


def _frontmatter(rec: dict) -> str:
    lines = ["---"]
    for k in FM_ORDER:
        if rec.get(k) not in (None, ""):
            lines.append(f"{k}: {_yaml(rec[k])}")
    lines.append("---")
    return "\n".join(lines)


def _read_rows(csv_path: Path) -> list[dict]:
    text = csv_path.read_text(encoding="utf-8")
    lines = [ln for ln in text.splitlines() if not ln.lstrip().startswith("#")]
    rows = list(csv.DictReader(io.StringIO("\n".join(lines))))
    return [r for r in rows if (r.get("url") or "").strip()]


def _load_manifest(path: Path) -> dict:
    by_id = {}
    if path.exists():
        for ln in path.read_text(encoding="utf-8").splitlines():
            ln = ln.strip()
            if ln:
                try:
                    r = json.loads(ln); by_id[r["id"]] = r
                except json.JSONDecodeError:
                    pass
    return by_id


def _write_manifest(path: Path, by_id: dict) -> None:
    with path.open("w", encoding="utf-8") as fh:
        for rid in sorted(by_id):
            fh.write(json.dumps(by_id[rid], ensure_ascii=False) + "\n")


def build(csv_path: Path, out: Path, force: bool = False, delay: float = 1.0) -> None:
    raw_dir, md_dir = out / "raw", out / "md"
    raw_dir.mkdir(parents=True, exist_ok=True)
    md_dir.mkdir(parents=True, exist_ok=True)
    manifest = out / "manifest.jsonl"
    by_id = _load_manifest(manifest)

    rows = _read_rows(csv_path)
    print(f"[{csv_path.name}] {len(rows)} rows")
    ok = skip = fail = paywall = 0
    for i, row in enumerate(rows, 1):
        url = row["url"].strip()
        rid = (row.get("id") or "").strip() or _auto_id(row, i)
        md_path = md_dir / f"{rid}.md"
        if md_path.exists() and not force:
            print(f"  skip {rid:34} (exists)"); skip += 1
            continue
        if _needs_institutional_access(url, row):
            # Paywalled / non-arXiv resolver: cannot be fetched openly. Skip cleanly
            # and continue; the open subset still gives the headline result.
            print(f"  skipped (needs institutional access): {rid}")
            paywall += 1
            continue
        if ok + fail > 0 and delay:
            time.sleep(delay)  # be polite to arXiv between fetches

        rec = {"id": rid, "source_url": url,
               "retrieved_at": datetime.now(timezone.utc).isoformat(timespec="seconds"),
               **{k: (row.get(k) or "").strip() for k in LABEL_COLS}}
        try:
            aid = _arxiv_id(url)
            if aid:
                paper = arxiv_lib.fetch_paper(aid)
                if paper["fulltext"]:
                    title, body = paper["title"], paper["markdown"]
                    rec.update(source_type="arxiv-html", fulltext=True, title=title,
                               sha256=hashlib.sha256(body.encode()).hexdigest(),
                               source_url=paper["source_url"])
                else:  # no LaTeXML HTML -> fall back to the arXiv PDF for full text
                    dl = fetch.download(f"https://arxiv.org/pdf/{aid}", raw_dir, rid)
                    if dl["ext"] == "pdf":
                        _t, body = convert.pdf_to_md(dl["path"])
                        title = paper["title"] or _t  # prefer authoritative arXiv title
                        rec.update(source_type="arxiv-pdf", fulltext=True,
                                   title=title, sha256=dl["sha256"],
                                   bytes=dl["bytes"], source_url=dl["final_url"])
                    else:  # last resort: abstract only
                        title, body = paper["title"], paper["markdown"]
                        rec.update(source_type="arxiv-abstract", fulltext=False, title=title,
                                   sha256=hashlib.sha256(body.encode()).hexdigest(),
                                   source_url=paper["source_url"])
            elif Path(url[7:] if url.startswith("file://") else url).exists():
                # local file (e.g. an institutional-access PDF in datasets/private/)
                local = url[7:] if url.startswith("file://") else url
                raw = Path(local).read_bytes()
                if raw[:4] == b"%PDF" or local.lower().endswith(".pdf"):
                    title, body = convert.pdf_to_md(local); st = "pdf-local"
                else:
                    title, body = convert.html_to_md(Path(local).read_text(errors="ignore")); st = "html-local"
                rec.update(source_type=st, fulltext=True, title=title,
                           sha256=hashlib.sha256(raw).hexdigest(), bytes=len(raw), source_url=local)
            else:
                dl = fetch.download(url, raw_dir, rid)
                rec.update(sha256=dl["sha256"], bytes=dl["bytes"], source_url=dl["final_url"])
                if dl["ext"] == "pdf":
                    title, body = convert.pdf_to_md(dl["path"]); rec.update(source_type="pdf", fulltext=True)
                elif dl["ext"] in ("html", "xml"):
                    title, body = convert.html_to_md(Path(dl["path"]).read_text(errors="ignore"))
                    rec.update(source_type="html", fulltext=True)
                else:
                    raise RuntimeError(f"unhandled content (ext={dl['ext']}, type={dl['content_type']})")
                rec["title"] = title
            rec["md_chars"] = len(body)
            md_path.write_text(_frontmatter(rec) + "\n\n# " + (rec.get("title") or rid) + "\n\n" + body + "\n",
                               encoding="utf-8")
            rec["md_path"] = str(md_path)
            rec["status"] = "ok"
            print(f"  ok   {rid:34} {rec['source_type']:10} {rec['md_chars']:>7} chars  {(rec.get('title') or '')[:46]}")
            ok += 1
        except Exception as e:  # noqa: BLE001 (report and continue; one bad link must not abort the build)
            rec.update(status="error", error=f"{type(e).__name__}: {e}")
            print(f"  FAIL {rid:34} {rec['error'][:78]}")
            fail += 1
        by_id[rid] = rec

    _write_manifest(manifest, by_id)
    print(f"[done] ok={ok} skip={skip} paywalled={paywall} fail={fail}  ->  {md_dir}  (manifest: {manifest})")
    if paywall:
        print(f"[note] {paywall} paper(s) skipped (paywalled / non-arXiv resolver, need institutional "
              f"access). The headline result holds on the open subset.")


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("csv", help="input CSV of resolver links")
    ap.add_argument("--out", default="data", help="output dir (default: data)")
    ap.add_argument("--force", action="store_true", help="rebuild even if Markdown exists")
    ap.add_argument("--delay", type=float, default=1.0, help="seconds between fetches (politeness)")
    a = ap.parse_args()
    build(Path(a.csv), Path(a.out), force=a.force, delay=a.delay)


if __name__ == "__main__":
    main()
