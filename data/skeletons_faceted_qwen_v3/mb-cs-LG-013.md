MECHANISM: The paper computes a gene prioritization framework that integrates multi-modal gene expression data with regulatory network structures using attention mechanisms. First, modality-specific variational autoencoders (VAEs) compress gene expression profiles from microarray, single-cell RNA-seq, and single-nucleus RNA-seq into latent representations. These latent vectors are concatenated to form a unified gene expression embedding. Next, gene regulatory networks (GRNs) are inferred independently from each modality using diverse algorithms, and random walks are generated from these networks to create text-like sequences. These sequences are embedded using a shared matrix and positional encodings, then processed by a transformer model trained via masked language modeling to produce global gene embeddings. A graph transformer module integrates these embeddings with positional encodings derived from graph Laplacian eigenvectors, protein-protein interaction scores, and Gene Ontology similarity. The graph transformer computes attention scores for each gene by jointly modeling network structure and expression context, producing a disease-specific relevance ranking. These scores are validated through gene set enrichment analysis to assess biological coherence. The method dynamically learns gene importance based on local and global network contexts, replacing static centrality measures with attention-driven relevance scoring. The framework preserves heavy-tailed network topology and enables extensibility to other diseases through modality-agnostic integration.  
DOMAIN: computational biology and gene prioritization  
STRUCTURE: graph traversal  
DATA_OBJECT: graph or network  
INFERENCE: deterministic or closed-form  
PROBLEM_FORM: ranking or retrieval  
DISTRIBUTION: none  
COMPLEXITY: not stated  
DATA_AVAILABILITY: none  
CODE_AVAILABILITY: none  
PREREGISTRATION: none  
EVIDENCE_BASIS: empirical-with-released-data
