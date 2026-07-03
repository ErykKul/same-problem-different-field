MECHANISM: The paper computes the positions, velocities, and accelerations of radioactive particles using an expectation-maximization (EM) algorithm applied to a Gaussian-mixture model. The model is defined over a set of lines derived from photon-pair detections in positron emission particle tracking (PEPT). The Gaussian-mixture includes components for real particle trajectories and spurious lines caused by scattering or random coincidences. Parameters include particle positions, activity levels, velocities, and accelerations. The EM algorithm alternates between an expectation step, which computes posterior probabilities of line assignments to particle components, and a maximization step, which updates parameters to maximize the likelihood. The method handles variable numbers of particles by allowing the number of components in the Gaussian mixture to change. Trajectory reconstruction is achieved by incorporating timing information from positron annihilations into the model. The algorithm is tested on simulated and experimental data, demonstrating robust tracking of up to 80 particles simultaneously. The method maps particle position estimates to full trajectories and accounts for uncertainty in the number of particles in the field of view. The Gaussian-mixture likelihood is maximized iteratively until convergence, with no closed-form solution required. The approach generalizes standard EM by adding velocity and acceleration parameters to the model.
DOMAIN: positron emission particle tracking
STRUCTURE: other: expectation-maximization
DATA_OBJECT: set or table
INFERENCE: deterministic or closed-form
PROBLEM_FORM: estimation
DISTRIBUTION: continuous; Gaussian
COMPLEXITY: not stated
DATA_AVAILABILITY: none
CODE_AVAILABILITY: none
PREREGISTRATION: none
EVIDENCE_BASIS: empirical-with-private-data
