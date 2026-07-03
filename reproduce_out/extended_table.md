# extended table

EXTENDED / wild run (incomplete labels): DETECTION. Headline = recall of known twins; AP is a lower bound.

| method | AP | AUROC | R@100 | R@1000 | R@3000 |
|---|---|---|---|---|---|
| abstract + TF-IDF (cheap) | 0.04 | 0.777 | 0.067 | 0.205 | 0.324 |
| abstract + SPECTER | 0.009 | 0.741 | 0.014 | 0.076 | 0.152 |
| abstract + SciNCL | 0.013 | 0.802 | 0.024 | 0.095 | 0.181 |
| abstract + SemCSE | 0.018 | 0.773 | 0.033 | 0.067 | 0.167 |
| abstract + Qwen3-Embedding-0.6B | 0.043 | 0.888 | 0.048 | 0.195 | 0.343 |
| abstract + E5-large-v2 | 0.015 | 0.734 | 0.033 | 0.086 | 0.167 |
| faceted-full + TF-IDF [Haiku (ours)] | 0.155 | 0.951 | 0.09 | 0.61 | 0.733 |
| faceted-full + TF-IDF [Opus] | 0.14 | 0.943 | 0.133 | 0.448 | 0.629 |
| faceted-full + TF-IDF [Qwen3-14b] | 0.079 | 0.932 | 0.071 | 0.433 | 0.629 |
| skeleton (MECHANISM) + TF-IDF [Haiku] | 0.258 | 0.925 | 0.219 | 0.524 | 0.652 |
