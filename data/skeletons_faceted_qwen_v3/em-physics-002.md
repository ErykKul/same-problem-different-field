MECHANISM: The paper computes the positions, velocities, and accelerations of particles using an expectation-maximization (EM) algorithm applied to a Gaussian mixture model defined over lines of response (LORs). The model incorporates both true LORs from particle annihilations and spurious LORs from scattering or random coincidences. The likelihood function is derived from a Gaussian mixture, where each component corresponds to a particle or an outlier. The EM algorithm iterates between an expectation step, which computes latent weights assigning each LOR to a particle or outlier, and a maximization step, which updates the parameters (positions, variances, and weights) of the Gaussian components. The positions are estimated as weighted centroids of LORs, variances are derived from the weighted distances between centroids and LORs, and weights are proportional to the number of assigned LORs. The algorithm is extended to track moving particles by parameterizing trajectories via Taylor expansions of position, velocity, and acceleration, allowing the reconstruction of time-dependent trajectories from temporally binned LOR data. The method is tested on simulated and experimental data, demonstrating robustness in tracking multiple particles simultaneously.  
DOMAIN: medical imaging  
STRUCTURE: other: expectation-maximization algorithm  
DATA_OBJECT: set or table  
INFERENCE: frequentist point estimate  
PROBLEM_FORM: estimation  
DISTRIBUTION: continuous; Gaussian  
COMPLEXITY: not stated  
DATA_AVAILABILITY: none  
CODE_AVAILABILITY: none  
PREREGISTRATION: none  
EVIDENCE_BASIS: simulation-study
