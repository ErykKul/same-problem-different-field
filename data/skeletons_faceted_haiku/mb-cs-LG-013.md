MECHANISM: Modality-specific variational autoencoders compress gene expression profiles from microarray, scRNA-seq, and snRNA-seq into latent representations. Gene regulatory networks are inferred independently from each modality. Random walks through inferred networks are tokenized and processed by a masked language model (BERT transformer) to learn global gene embeddings capturing regulatory structure across modalities. Gene positional encodings are derived from graph Laplacian eigenvectors. A graph transformer integrates multi-modal expression embeddings, network structure via positional encodings, and auxiliary biological networks (PPI, Gene Ontology, diffusion-based similarity). Attention mechanisms assign NETRA scores quantifying disease-specific gene relevance. Gene rankings and attention maps identify prioritized candidate genes and reveal regulatory relationships.

DOMAIN: computational biology, gene prioritization, graph neural networks

STRUCTURE: graph traversal

DATA_OBJECT: graph or network

INFERENCE: optimization only

PROBLEM_FORM: ranking or retrieval

DISTRIBUTION: not stated

COMPLEXITY: not stated
