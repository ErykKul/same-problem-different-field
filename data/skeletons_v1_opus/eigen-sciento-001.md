MECHANISM: A weighted directed network of entities is encoded as a square matrix whose entries count directed references from one entity to another over a window, with diagonal entries zeroed to remove self-loops. Each column is divided by its sum to produce a column-stochastic transition matrix giving the conditional probability of moving along an edge. Columns corresponding to entities with no outgoing weight are replaced by a fixed normalized weighting vector so every column sums to one. A second operator is formed as a convex combination of this transition matrix and a rank-one matrix whose columns equal the weighting vector, mixing edge-following with random restart at rate controlled by a damping parameter. This combined operator defines a stationary process whose long-run occupation of each entity is sought. The leading eigenvector of the operator is extracted, giving the steady-state occupation fractions. This eigenvector is then mapped through the transition structure and normalized to percentages to obtain an importance score per entity. The procedure weights incoming edges by the importance of their source, so an entity is important when referenced by other important entities. The result is a single scalar ranking value for each node of the network.
DOMAIN: scientometrics and journal citation analysis
STRUCTURE: spectral or transform
DATA_OBJECT: graph or network
INFERENCE: deterministic or closed-form
PROBLEM_FORM: ranking or retrieval
DISTRIBUTION: count; none
COMPLEXITY: closed-form
