MECHANISM: A square nonnegative matrix is constructed whose entries count directed interactions from one entity to another over a fixed window, and the diagonal entries are set to zero to remove self-interactions. Each column is divided by its sum so the matrix becomes column-stochastic, encoding transition probabilities between entities. Columns that are entirely zero (entities with no outgoing weight) are replaced by a fixed probability vector whose entries are proportional to each entity's size. A new stochastic matrix is then formed as a convex combination: with probability α a transition follows the normalized interaction matrix, and with probability 1−α it jumps to an arbitrary entity according to the size-proportional vector. This convex combination defines an irreducible, aperiodic transition matrix of a discrete-time Markov chain. The leading (dominant) eigenvector of this matrix, equivalently the stationary distribution of the chain, is computed iteratively. This eigenvector assigns each entity a steady-state weight reflecting long-run occupancy. Final scores are obtained by multiplying the normalized interaction matrix by this weight vector and rescaling the result to sum to a constant, so that incoming interactions are weighted by the importance of their source. Entities are then ranked by these scores.
DOMAIN: scientometrics; bibliometric journal citation ranking
STRUCTURE: spectral or transform
DATA_OBJECT: graph or network
INFERENCE: deterministic or closed-form
PROBLEM_FORM: ranking or retrieval
DISTRIBUTION: none
COMPLEXITY: not stated
