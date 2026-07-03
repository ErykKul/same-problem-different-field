MECHANISM: The paper computes a reweighted path ensemble by combining multiple trajectory ensembles conditioned on different collective variables. It uses the Multistate Bennett Acceptance Ratio (MBAR) methodology to estimate path weights and partition sums that recover an unbiased ensemble from biased samples. The process involves maximizing the likelihood of observing sampled trajectories under conditional ensembles, leading to a fixed-point equation for weights. Each trajectory's weight depends on the maximum interface it crosses, determined by a quantity associated with the trajectory. The method generalizes to arbitrary numbers of interface sets by jointly solving equations derived from likelihood maximization over all ensembles. The resulting weights are used to construct an unbiased probability distribution over paths, which enables accurate estimation of crossing probabilities and rate constants. The approach iteratively solves equations involving sums over trajectories, partition sums, and indicator functions that encode conditional sampling constraints. The final reweighted ensemble combines contributions from all interface sets, ensuring consistency between forward and reverse transitions through flux-matching constraints. The method is validated using toy models and host-guest systems, demonstrating improved statistical accuracy compared to naive combinations.
DOMAIN: molecular simulation
STRUCTURE: other: likelihood-based optimization
DATA_OBJECT: sequence or time-series
INFERENCE: optimization only
PROBLEM_FORM: estimation
DISTRIBUTION: binary; binary
COMPLEXITY: not stated
DATA_AVAILABILITY: none
CODE_AVAILABILITY: none
PREREGISTRATION: none
EVIDENCE_BASIS: simulation-study
