MECHANISM: The paper computes a sequence alignment method using a self-supervised Transformer model to generate vector embeddings of DNA subsequences. The model is trained with a contrastive loss to minimize the distance between embeddings of similar sequences (positive pairs) and maximize it for dissimilar ones (negative pairs). Embeddings are generated for both reads and reference genome fragments, which are stored in a vector database. For alignment, the read's embedding is queried against the database to retrieve top-K fragments with nearest embeddings. These fragments are then aligned to the read using a Smith-Waterman (SW) algorithm to find the optimal match. The method relies on sharding the reference genome into overlapping fragments of length comparable to the read length, ensuring coverage and reducing search complexity. The contrastive loss enforces that embeddings of aligned read-fragment pairs are closer than those of misaligned pairs. The vector store enables efficient nearest-neighbor search, reducing the problem from scanning the entire genome to querying a logarithmic-scale database. The SW alignment step refines the candidate fragments to determine the exact genomic position. The model's training involves dropout masks and temperature scaling to stabilize learning. The method is evaluated on simulated reads with varying mutation rates and quality scores, using recall metrics to assess alignment accuracy. The framework is designed to handle noisy reads by incorporating mutations during training and using a combination of mean and max-pooling baselines for comparison. The computational steps include embedding generation, vector database indexing, nearest-neighbor retrieval, and SW alignment optimization.

DOMAIN: bioinformatics, DNA sequence alignment

STRUCTURE: map-reduce or embarrassingly-parallel

DATA_OBJECT: sequence or time-series

INFERENCE: deterministic or closed-form

PROBLEM_FORM: search

DISTRIBUTION: none

COMPLEXITY: polynomial iterative

DATA_AVAILABILITY: dataset-with-DOI-or-handle

CODE_AVAILABILITY: public-repository

PREREGISTRATION: none

EVIDENCE_BASIS: empirical-with-released-data
