MECHANISM: Compute a two-dimensional matrix of alignment scores via dynamic programming recurrence over two sequences; at each matrix cell (i,j) compute the maximum of three dependencies (diagonal, left, upper) incorporating match/mismatch costs and gap penalties; parallelize by mapping matrix cells to GPU threads organized in warps, storing intermediate values in thread-local registers and using low-latency shuffle operations between neighboring threads; minimize global memory accesses using register tiling and intra-warp communication; optionally trace back to recover the alignment path.
DOMAIN: Bioinformatics, sequence alignment acceleration
STRUCTURE: dynamic programming
DATA_OBJECT: sparse matrix
INFERENCE: deterministic or closed-form
PROBLEM_FORM: optimization
DISTRIBUTION: none
COMPLEXITY: polynomial iterative
