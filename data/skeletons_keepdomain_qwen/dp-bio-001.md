MECHANISM: The paper computes a dynamic programming (DP) alignment algorithm optimized for GPU execution. It initializes a DP matrix for sequence alignment, where each cell represents the alignment score between subsequences. To reduce memory access latency, the method employs warp shuffles to share data between threads within a warp, minimizing global memory transactions. Half-precision floating-point arithmetic is used to reduce memory bandwidth requirements and improve computational throughput. The algorithm processes multiple sequence pairs in parallel by partitioning the DP matrix across GPU threads. The method avoids explicit memory transfers between host and device by keeping intermediate results in GPU memory. The alignment score is computed iteratively across the DP matrix, with each step depending on previously computed values. The final alignment is reconstructed by backtracking through the DP matrix using stored pointers. The approach is applied to sequence alignment in bioinformatics, specifically for next-generation sequencing (NGS) reads. The optimization targets the memory-bound nature of DP on GPUs by leveraging warp-level parallelism and reduced precision. The method is implemented as a library (AnySeq/GPU) that integrates with existing sequence alignment tools. The paper evaluates the performance gains achieved through these optimizations on real NGS datasets.
DOMAIN: bioinformatics - sequence alignment
STRUCTURE: dynamic programming
DATA_OBJECT: sequence or time-series
INFERENCE: deterministic or closed-form
PROBLEM_FORM: optimization
DISTRIBUTION: none
COMPLEXITY: not stated
DATA_AVAILABILITY: none
CODE_AVAILABILITY: public-repository
PREREGISTRATION: none
EVIDENCE_BASIS: empirical-with-released-data
