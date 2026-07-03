MECHANISM: The paper computes a structural reducibility measure for hypergraphs using information-theoretic principles. It defines a coarse-grained representation of a hypergraph by grouping nodes according to an arbitrary partition, then calculates the information content required to transmit layers of the hypergraph under this partition. The method involves computing multiset intersections, entropy-based measures of redundancy, and optimizing over subsets of representative layers to minimize information transmission costs. A reducibility measure η(b) is derived as the ratio of the difference between maximum and minimum information costs under a given partition. The algorithm iteratively evaluates overlaps between hyperedge layers, computes logarithmic terms based on multiset coefficients, and determines optimal representative layers through optimization. The measure quantifies how much structural redundancy exists in a hypergraph when compressed under a specific node grouping, with η(b) ∈ [0,1] indicating maximal to minimal compressibility. The method extends to multiscale reducibility by considering multiple layers of interactions and their overlaps, and applies to both synthetic and real-world hypergraphs through entropy-based similarity metrics. Reducibility is evaluated per layer and across the entire hypergraph, with results validated through synthetic experiments and empirical datasets.
DOMAIN: hypergraph structural analysis
STRUCTURE: other: information-theoretic optimization
DATA_OBJECT: multiset of tuples
INFERENCE: deterministic or closed-form
PROBLEM_FORM: estimation
DISTRIBUTION: none
COMPLEXITY: not stated
DATA_AVAILABILITY: none
CODE_AVAILABILITY: none
PREREGISTRATION: none
EVIDENCE_BASIS: simulation-study
