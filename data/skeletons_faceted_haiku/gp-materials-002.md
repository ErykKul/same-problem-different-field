MECHANISM: Constructs a deep Gaussian process (DGP) surrogate model for multi-objective materials property prediction from heterotopic, multi-fidelity data. Stacks multiple latent GP layers to learn shared representations of material properties and their correlations. Uses Whittle approximation or variational inference to handle computational scalability. Integrates the DGP with a cost-aware batch Bayesian optimization framework: selects candidate materials via q-Expected Hypervolume Improvement (qEHVI) acquisition, weighted by evaluation costs across different fidelity levels. Iteratively refines the surrogate and acquisition strategy to balance exploration versus exploitation under budget constraints.
DOMAIN: Materials science, Bayesian optimization, high-entropy alloy discovery
STRUCTURE: other: kernel-based regression
DATA_OBJECT: dense matrix or tensor
INFERENCE: Bayesian posterior
PROBLEM_FORM: optimization
DISTRIBUTION: continuous; continuous
COMPLEXITY: polynomial iterative
