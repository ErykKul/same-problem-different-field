MECHANISM: Develop effective sample size (ESS) measures for assessing Markov chain Monte Carlo mixing quality in Bayesian phylogenetic inference. Extend classical ESS definitions (originally for continuous scalar parameters) to discrete tree topologies, which are high-dimensional complex objects. Propose multiple ESS approaches: (A) generalizing continuous variable ESS identities to trees; (B) computing ESS on reduced-dimensional representations; (C) ad-hoc methods. Validate each candidate ESS measure by comparing two Monte Carlo estimates: standard errors from actual MCMC runs versus standard errors from independent samples sized according to the computed ESS. Apply the approach to three phylogenetic summaries: split (edge) probabilities, tree topology probabilities, and summary trees. Select ESS measures that accurately capture Monte Carlo error across these summaries, enabling practitioners to assess convergence of tree topology mixing.
DOMAIN: Phylogenetics, Bayesian inference, evolutionary biology
STRUCTURE: graphical models
DATA_OBJECT: tree or hierarchy
INFERENCE: Bayesian posterior
PROBLEM_FORM: estimation
DISTRIBUTION: none
COMPLEXITY: not stated
