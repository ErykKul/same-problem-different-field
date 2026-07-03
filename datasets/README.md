# Datasets: the link lists

The corpus is not stored here. What is versioned is a pair of **link lists**: CSV
files where each row points at one paper. `src/build_dataset.py` reads a link
list, fetches each paper from arXiv or an open URL, converts the PDF or HTML to
Markdown, and writes the result under `data/`. Freezing the links (rather than the
papers) keeps the package small, license-clean, and reproducible: the same list
plus the same fetch code gives the same corpus.

Two lists:

| file | mode | labels | role |
|---|---|---|---|
| `mode_a_seed_families.csv` | A (curated) | complete | the benchmark where methods are compared; grouped into structural families |
| `mode_b_discovery.csv` | B (extended) | none (unlabeled background) | the wild detection run; a frozen cross-domain arXiv sample |

## Schema

Both files are CSV with a header row. Lines beginning with `#` are comments. All
columns except `url` are optional; the label columns are copied verbatim into each
paper's Markdown front-matter and into `data/manifest.jsonl`.

| column | meaning |
|---|---|
| `id` | short stable slug for the paper (used as the Markdown filename). If blank it is auto-generated from `family` + `field`. |
| `url` | an arXiv link or id (`https://arxiv.org/abs/2401.18059`, `arxiv.org/pdf/...`, or a bare `2401.18059`), or any openly fetchable PDF / HTML URL. |
| `family` | structural-family key (Mode A only): every member of a family shares the same underlying computation, across different fields. This defines the ground-truth twin pairs. |
| `field` | the paper's domain / discipline (or its arXiv category in Mode B). A twin pair is a same-`family`, different-`field` pair. |
| `role` | `member` (a genuine instance of the family) or `distractor` (a same-field paper with different math, included as a hard negative). |
| `method_named` | `yes` / `no` / `?`: does the paper name its method on the page. The `no` rows test real abstraction rather than name recognition. |
| `license` | OA license or source tag if known (governs redistribution of any derived Markdown). |
| `note` | free text. |

Mode A carries the full label set; Mode B uses only `id, url, field, license, note`
(it is an unlabeled background, regenerable with `src/sample_arxiv.py`).

## Paywalled rows (institutional access)

Some source papers live behind a publisher paywall, reached through a non-arXiv
resolver (for example a bare `doi.org` link with no open copy). The **public build
cannot fetch these without institutional access**, so it skips them cleanly:

```
skipped (needs institutional access): <id>
```

and continues with the rest. You still get a strong result on the open subset
(about 216 of the 236 labelled twins), and the method ranking is unchanged. The
full numbers reported in the paper assume every paper is present. If you do have
institutional access you can download such a paper by hand and point its row at a
local file (`file:///abs/path.pdf`), which the build fetches via its local-file
path.
