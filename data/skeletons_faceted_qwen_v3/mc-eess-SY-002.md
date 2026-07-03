MECHANISM: The paper computes the relationship between network clustering and the minimum number of driver/observer nodes required for controllability/observability in complex networks. It models networks as undirected graphs, defines observability as inferring system states from measured outputs and controllability as influencing system behavior via inputs. The method uses graph-theoretic concepts, including bipartite graph representations, max matching algorithms, and the Dulmage-Mendelsohn decomposition to identify unmatched nodes. These unmatched nodes determine the minimal number of driver/observer nodes required. The paper compares two network models (Barabási-Albert and Holme-Kim) with differing clustering properties, quantifies their clustering coefficients, and simulates how varying clustering affects the number of unmatched nodes. It applies Monte-Carlo simulations to analyze large-scale networks and demonstrates that increasing clustering reduces unmatched nodes. The method involves adding links to networks to alter clustering coefficients and re-evaluating unmatched nodes. The paper also provides case studies on real-world networks, adjusting their clustering and measuring changes in unmatched nodes. The computational steps include graph construction, matching computation, decomposition, and statistical analysis of results across network sizes and structures.  
DOMAIN: complex networks and systems theory  
STRUCTURE: graph traversal  
DATA_OBJECT: graph or network  
INFERENCE: deterministic or closed-form  
PROBLEM_FORM: estimation  
DISTRIBUTION: none  
COMPLEXITY: polynomial iterative  
DATA_AVAILABILITY: public-benchmark-used  
CODE_AVAILABILITY: none  
PREREGISTRATION: none  
EVIDENCE_BASIS: empirical-with-released-data
