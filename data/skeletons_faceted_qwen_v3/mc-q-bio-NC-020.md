MECHANISM: The paper computes a stochastic model of neural activity and movement. It generates synthetic place fields using Gaussian distributions with randomized parameters, simulates mouse trajectories via a biased random walk with diffusion, and filters trajectory data by velocity thresholds. The model estimates neural flow as the integral of firing rate gradients over space and time. Place fields are parameterized with mean positions, widths, and firing rates, with noise added to each bin. Trajectory simulations use a stochastic differential equation with drift velocity and diffusion coefficient. The reward zone is identified by segmenting the track into bins and removing sections with velocities below a threshold. Neural flow is validated by comparing simulated outputs to empirical measurements. The model assumes stationarity in place field statistics and constant velocity during non-reward periods. Parameters are estimated by fitting simulated flows to experimental data, excluding reward zone segments. The computation involves generating synthetic data, solving differential equations, and applying threshold-based filtering.
DOMAIN: computational neuroscience
STRUCTURE: other: stochastic simulation
DATA_OBJECT: point set
INFERENCE: deterministic or closed-form
PROBLEM_FORM: simulation or generation
DISTRIBUTION: continuous; continuous
COMPLEXITY: not stated
DATA_AVAILABILITY: public-repository
CODE_AVAILABILITY: public-repository
PREREGISTRATION: none
EVIDENCE_BASIS: empirical-with-private-data
