MECHANISM: The paper computes network-based bibliometric analysis by constructing graphs where nodes represent entities (e.g., articles, authors) and edges represent relationships (e.g., citations, co-authorships). The process begins by querying a database to retrieve entities and their connections, forming a graph structure. Nodes are defined by metadata, and edges are established based on predefined relationships. The graph is then analyzed using centrality metrics (e.g., betweenness, eigenvector centrality) to quantify the importance of nodes. Community detection algorithms (e.g., Louvain, Infomap) are applied to identify clusters of densely connected nodes, revealing thematic or collaborative structures. The analysis includes expanding the graph by incorporating base set nodes, which are indirectly connected to the root set, to capture broader contextual relationships. Visualization tools generate graphical representations of the network, and clustering techniques are used to explore thematic patterns. The methods rely on deterministic algorithms without probabilistic assumptions, focusing on structural properties rather than statistical inference. The computational steps are modular, separating data collection, graph construction, and analysis phases. The library integrates with external APIs to retrieve data, ensuring flexibility in data sources and formats. The output includes metrics, visualizations, and cluster assignments, enabling users to interpret network structures and relationships.
DOMAIN: bibliometric analysis
STRUCTURE: graph traversal
DATA_OBJECT: graph or network
INFERENCE: deterministic or closed-form
PROBLEM_FORM: analysis
DISTRIBUTION: none
COMPLEXITY: not stated
DATA_AVAILABILITY: public-benchmark-used
CODE_AVAILABILITY: public-repository
PREREGISTRATION: none
EVIDENCE_BASIS: empirical-with-released-data
