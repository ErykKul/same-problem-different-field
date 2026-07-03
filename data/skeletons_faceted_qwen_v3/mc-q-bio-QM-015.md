MECHANISM: The paper computes a generative model of spatial network morphogenesis using stochastic rules for branching, fusion, and stopping during elongation. The process begins with a star-shaped network initialized with a root node and multiple active tips. At each time step, each active tip independently attempts an elongation event, which can be growth (extending the tip by a fixed length) or branching (creating two new edges at a fixed angle, increasing the number of active tips). Before elongation, the tip checks for potential intersections within a sensing distance; if an intersection is detected, the tip becomes inactive with a given probability (representing growth arrest), or elongation proceeds. If an actual geometric intersection occurs during elongation, the segments deterministically fuse by inserting a new node at the intersection point. The process terminates when the total network length reaches a predefined value. The model generates a morphospace of network architectures by varying branching and stopping probabilities, and evaluates these networks on three performance objectives: transport efficiency (measured via conductance between boundaries), robustness to damage (measured via the area under the curve of largest connected component length after random edge removal), and space exploration (measured via the buffered area of the network). The model quantifies trade-offs between these objectives using a Pareto front analysis, showing that synthetic networks produced by the model occupy similar regions of performance space as empirical fungal networks. The computational steps involve probabilistic decision-making, geometric intersection detection, and topological modification through fusion, all operating on a planar graph structure without global optimization or feedback mechanisms.
DOMAIN: biological network morphogenesis
STRUCTURE: other: stochastic growth rules
DATA_OBJECT: graph or network
INFERENCE: none
PROBLEM_FORM: optimization
DISTRIBUTION: none
COMPLEXITY: not stated
DATA_AVAILABILITY: public-benchmark-used
CODE_AVAILABILITY: none
PREREGISTRATION: none
EVIDENCE_BASIS: empirical-with-released-data
