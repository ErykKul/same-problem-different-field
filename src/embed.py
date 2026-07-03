"""Stage 3a: turn a chosen text representation of each paper into vectors.

Representations:
  abstract : the paper's abstract (topical baseline), extracted from data/md
  skeleton : the distilled computational skeleton (data/skeletons) -- ours
  full     : the whole cleaned md body

Methods:
  tfidf       : scikit-learn TF-IDF (torch-free; the cheap first-pass instrument)
  st:<model>  : sentence-transformers (semantic; needs the heavier ML extras)

The probe's headline is the CONTRAST between skeleton and abstract under the same
method, so a cheap method is fine for a first signal; swap in a semantic embedder
for the real run.
"""
from __future__ import annotations
import re
from pathlib import Path
import numpy as np


def extract_abstract(md_text: str) -> str:
    body = re.sub(r"^---\n.*?\n---\n", "", md_text, flags=re.S)  # drop front-matter
    m = re.search(r"##\s*Abstract\s*(.+?)(?:\n#|\Z)", body, flags=re.S | re.I)
    if m and len(m.group(1).strip()) > 80:
        return " ".join(m.group(1).split())
    # fallback: first ~1200 chars of body (title + abstract + intro start)
    body = re.sub(r"^#\s+.*\n", "", body)  # drop the H1 title line
    return " ".join(body.split())[:1200]


def load_rep(data_dir: str | Path, rep: str) -> dict[str, str]:
    data_dir = Path(data_dir)
    out: dict[str, str] = {}
    if rep == "skeleton":
        for p in (data_dir / "skeletons").glob("*.md"):
            out[p.stem] = p.read_text(encoding="utf-8").strip()
    else:
        for p in (data_dir / "md").glob("*.md"):
            txt = p.read_text(encoding="utf-8")
            out[p.stem] = extract_abstract(txt) if rep == "abstract" else \
                re.sub(r"^---\n.*?\n---\n", "", txt, flags=re.S).strip()
    return out


def embed_texts(texts: list[str], method: str = "tfidf") -> np.ndarray:
    if method == "tfidf":
        from sklearn.feature_extraction.text import TfidfVectorizer
        X = TfidfVectorizer(stop_words="english", min_df=1, sublinear_tf=True,
                            ngram_range=(1, 2)).fit_transform(texts)
        return X.toarray().astype(np.float32)
    if method.startswith("st:"):
        from sentence_transformers import SentenceTransformer
        name = method[3:]
        if "e5" in name.lower():  # E5 expects a query:/passage: prefix; symmetric paper-paper task -> query
            texts = ["query: " + t for t in texts]
        m = _ST_CACHE.get(name)
        if m is None:
            m = _ST_CACHE[name] = SentenceTransformer(name)  # load ONCE, reuse across calls
        return np.asarray(m.encode(texts, normalize_embeddings=True), dtype=np.float32)
    raise ValueError(f"unknown method {method!r}")


_ST_CACHE: dict = {}


def l2norm(X: np.ndarray) -> np.ndarray:
    n = np.linalg.norm(X, axis=1, keepdims=True)
    n[n == 0] = 1.0
    return X / n


def cosine_matrix(X: np.ndarray) -> np.ndarray:
    Xn = l2norm(X)
    return Xn @ Xn.T
