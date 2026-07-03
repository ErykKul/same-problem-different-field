MECHANISM: A pharmacology knowledge graph is constructed from structured database records with entities (drugs, proteins, indications) and edges (relations between them). Knowledge graph embedding models learn low-dimensional representations of entities by optimizing a scoring function that preserves observed edges while minimizing scores for missing edges. Graph neural networks with attention mechanisms encode categorical node features (protein embeddings from language models) and topological structure. Models are evaluated on link prediction tasks using PR-AUC metric, systematically varying model size, data volume, and feature modalities. Temporal validation ensures test data are from a later period than training.
DOMAIN: drug repurposing and knowledge graphs
STRUCTURE: graph traversal
DATA_OBJECT: graph or network
INFERENCE: frequentist point estimate
PROBLEM_FORM: prediction or classification
DISTRIBUTION: binary
COMPLEXITY: polynomial iterative
