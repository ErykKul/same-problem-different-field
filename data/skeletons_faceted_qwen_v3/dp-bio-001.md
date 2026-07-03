MECHANISM: The paper computes a dynamic programming (DP) alignment of two sequences by iteratively evaluating recurrence relations that depend on neighboring cells in a matrix. The method partitions the DP matrix into submatrices processed in parallel by thread groups, with each thread computing a subset of cells using in-register arithmetic to minimize memory access. Warp shuffles enable low-latency communication between threads to share intermediate values, reducing global memory traffic. The algorithm supports different alignment types (local, global, semi-global) by adjusting initialization conditions and gap penalty schemes (linear or affine). For each cell, the recurrence relation computes the maximum of three possibilities: extending a match, inserting a gap in the query sequence, or inserting a gap in the subject sequence. The method uses half-precision arithmetic to reduce memory bandwidth requirements and employs a scoring profile stored in shared memory to accelerate substitution score lookups. The DP matrix is partitioned to fit within register limits, and workload is distributed across stages to handle long sequences. Traceback is implemented in linear space by storing predecessor information during the forward pass. The algorithm is optimized for GPU architectures by leveraging warp-level parallelism and minimizing divergent execution paths through uniform data access patterns.
DOMAIN: bioinformatics
STRUCTURE: dynamic programming
DATA_OBJECT: dense matrix
INFERENCE: deterministic or closed-form
PROBLEM_FORM: estimation
DISTRIBUTION: none
COMPLEXITY: not stated
DATA_AVAILABILITY: public-benchmark-used
CODE_AVAILABILITY: public-repository
PREREGISTRATION: none
EVIDENCE_BASIS: empirical-with-released-data
