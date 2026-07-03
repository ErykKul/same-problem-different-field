MECHANISM: The method constructs a topological representation of a multivariate point cloud by covering the data with overlapping balls of fixed radius ε. Each ball is centered on a randomly selected data point, and all points within ε distance are included in the ball. The algorithm iteratively selects new centers from uncovered points until all data are covered. Overlapping balls are connected by edges, forming a graph that encodes spatial relationships. The size of each ball's representation in the output corresponds to the number of points it contains, and the graph is colored based on a separate variable Y, which may be a function of the data or model residuals. The process is deterministic, with no probabilistic modeling or optimization involved. The output graph preserves the relative density and connectivity of the original data, allowing visualization of structure without dimensionality reduction. The algorithm does not require parameter tuning for ε beyond user selection, though sensitivity to ε is acknowledged. The final graph is an abstract 2D representation of the K-dimensional data, with no inherent coordinate system. The method is applied to both synthetic and real-world datasets to demonstrate its utility in revealing patterns, model residuals, and variable interactions.
DOMAIN: topological data analysis
STRUCTURE: other: ball-based cover
DATA_OBJECT: point set
INFERENCE: deterministic or closed-form
PROBLEM_FORM: estimation
DISTRIBUTION: none
COMPLEXITY: not stated
DATA_AVAILABILITY: public-benchmark-used
CODE_AVAILABILITY: public-repository
PREREGISTRATION: none
EVIDENCE_BASIS: empirical-with-released-data
