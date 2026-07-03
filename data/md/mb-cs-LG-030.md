# mb-cs-LG-030

## Abstract

The recent works on causal discovery have followed a similar trend of learning partial ancestral graphs (PAGs) since observational data constrain the true causal directed acyclic graph (DAG) only up to a Markov equivalence class. This limits their application in the majority of downstream tasks, as uncertainty in causal relations remains unresolved. We propose a new refinement framework, CausalSAGE, for converting PAGs to DAGs while respecting the underlying causal relations. The framework expands discrete variables into state-level representations, constrains the search space using structural knowledge and soft priors, and applies a unified differentiable objective for joint optimization. The final DAG is obtained by aggregating the optimized structures and enforcing acyclicity when necessary. Our experimental evaluations show that the obtained DAGs preserve the underlying causal relations while also being efficient to obtain.
