MECHANISM: A graph encoder decomposes node neighborhoods into distance-aware channels by extracting exact k-hop neighbors independently. Each hop is then processed through frequency-based channels that split signals into low-pass (smooth) and high-pass (contrasting) components via graph Laplacian filtering. Within each hop, low- and high-frequency representations are fused via attention. Final node embeddings concatenate fused representations across all hops and pass through an MLP to produce compact unified embeddings. During search, a signed community construction builds a positive graph from embedding similarities, and an adaptive scoring function balances embedding similarity and topological cohesiveness based on the graph's estimated homophily ratio.
DOMAIN: Graph neural networks for community detection on heterophilic graphs
STRUCTURE: graph traversal
DATA_OBJECT: graph or network
INFERENCE: deterministic or closed-form
PROBLEM_FORM: search
DISTRIBUTION: none
COMPLEXITY: polynomial iterative
