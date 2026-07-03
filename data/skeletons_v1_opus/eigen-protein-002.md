MECHANISM: A set of entities is represented as nodes of a weighted graph whose edge weights encode pairwise statistical dependence between the fluctuating quantities attached to each pair. A dependence coefficient is derived from an information-theoretic measure (marginal and joint entropies of the pair) and optionally rescaled by an exponentially decaying function of the inter-node separation with a tunable locality length. These weights populate a symmetric nonnegative square matrix with zero diagonal. The dominant invariant direction of this matrix is extracted by eigen-decomposition, retaining the eigenvector associated with the largest eigenvalue. Because the matrix is symmetric with nonnegative entries, this leading eigenvector is unique and has nonnegative components, which are interpreted as a per-node importance score; the squared components sum to one and act like a stationary weight. The associated eigenvalue summarizes overall connectivity strength. A second, neighborhood-adjusted score is formed by subtracting a degree-like aggregate from the centrality. Differences of these scores between two regimes of the system localize the nodes whose importance shifts most. Sweeping the locality length separates short-range from long-range contributions to the importance pattern.
DOMAIN: protein biophysics and allosteric signaling
STRUCTURE: spectral or transform
DATA_OBJECT: graph or network
INFERENCE: deterministic or closed-form
PROBLEM_FORM: ranking or retrieval
DISTRIBUTION: continuous; none
COMPLEXITY: closed-form
