# curated table

CURATED benchmark (complete labels): COMPARE methods. Headline = AP.

| method | AP | AUROC | R@50 | R@100 | R@200 |
|---|---|---|---|---|---|
| abstract + TF-IDF (cheap) | 0.222 | 0.738 | 0.114 | 0.2 | 0.3 |
| abstract + SPECTER | 0.095 | 0.656 | 0.057 | 0.071 | 0.119 |
| abstract + SciNCL | 0.149 | 0.776 | 0.081 | 0.124 | 0.181 |
| abstract + SemCSE | 0.141 | 0.757 | 0.062 | 0.105 | 0.171 |
| abstract + Qwen3-Embedding-0.6B | 0.226 | 0.834 | 0.095 | 0.171 | 0.286 |
| abstract + E5-large-v2 | 0.144 | 0.726 | 0.067 | 0.11 | 0.19 |
| faceted-full + TF-IDF [Haiku (ours)] | 0.557 | 0.928 | 0.181 | 0.352 | 0.557 |
| faceted-full + TF-IDF [Opus] | 0.533 | 0.912 | 0.214 | 0.338 | 0.495 |
| faceted-full + TF-IDF [Qwen3-14b] | 0.396 | 0.88 | 0.162 | 0.29 | 0.405 |
| skeleton (MECHANISM) + TF-IDF [Haiku] | 0.513 | 0.879 | 0.2 | 0.352 | 0.51 |
