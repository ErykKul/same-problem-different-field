MECHANISM: Compute optimal global alignment of two character sequences (phonetic IPA transcriptions) via dynamic programming; fill a two-dimensional matrix where each cell represents the best alignment score for sequence prefixes; at each cell choose the maximum of three options (match/mismatch from diagonal, gap from above, gap from left) according to similarity function and gap penalty; parallelize by assigning each thread to compute one pairwise alignment in the adjacency matrix; store intermediate scores in shared GPU memory for efficient access.
DOMAIN: Computational linguistics, phonetic similarity
STRUCTURE: dynamic programming
DATA_OBJECT: sequence or time-series
INFERENCE: deterministic or closed-form
PROBLEM_FORM: optimization
DISTRIBUTION: none
COMPLEXITY: polynomial iterative
