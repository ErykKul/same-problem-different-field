MECHANISM: A Transformer encoder model learns to embed DNA sequences into a shared vector space using contrastive self-supervised learning. The model maps reads and reference genome fragments to fixed-size embeddings such that similar sequences map to nearby points. The Embed-Search-Align framework shards the reference genome into overlapping fragments, encodes all fragments once into a vector database, then for each read performs nearest-neighbor search in embedding space to retrieve candidate fragments followed by fine-grained Smith-Waterman alignment.
DOMAIN: genomics; sequence alignment; bioinformatics
STRUCTURE: other: transformer embeddings with vector search
DATA_OBJECT: sequence or time-series
INFERENCE: contrastive self-supervised learning; nearest-neighbor search in embedding space
PROBLEM_FORM: search; ranking or retrieval
DISTRIBUTION: none
COMPLEXITY: polynomial iterative
