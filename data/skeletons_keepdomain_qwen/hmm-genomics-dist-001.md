MECHANISM: The paper computes a sequence alignment method using a self-attention-based neural network (Transformer) to generate vector embeddings of DNA reads and reference genome fragments. The model is trained with a contrastive loss function to maximize similarity between embeddings of matching sequences while minimizing similarity between non-matching pairs. Embeddings are generated in a shared vector space where read-fragment distance metrics approximate sequence similarity. A DNA vector store is constructed to index reference fragment embeddings for efficient global search. During alignment, read embeddings are queried against the vector store using nearest-neighbor search to identify candidate reference locations. The method avoids explicit genome indexing by relying on the embedding space's structure for search. The framework is evaluated on human reference genomes and tested across chromosomes and species. The model's accuracy is measured by comparing alignment results to conventional methods like Bowtie and BWA-Mem. The contrastive loss enables self-supervised training without labeled alignment data. The vector store's design allows sublinear-time search over the reference genome. The method's performance is validated on 250-length reads aligned to a 3-gigabase human genome.
DOMAIN: genomics and sequence alignment
STRUCTURE: other: neural network-based
DATA_OBJECT: sequence or time-series; dense matrix or tensor
INFERENCE: deterministic or closed-form
PROBLEM_FORM: search
DISTRIBUTION: none
COMPLEXITY: not stated
DATA_AVAILABILITY: public-benchmark-used
CODE_AVAILABILITY: none
PREREGISTRATION: none
EVIDENCE_BASIS: empirical-with-released-data
