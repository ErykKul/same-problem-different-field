MECHANISM: Fit a self-exciting space-time point process whose conditional intensity is a constant background rate plus a sum of triggering kernels from past events. Each event's triggering productivity scales with an associated mark, its temporal influence decays as a power law, and its spatial influence decays with distance. Estimate the parameters by maximum likelihood, alternating between soft-attributing each event to the background or to a triggering parent and re-estimating the rate and kernel parameters from those attributions. Allow the parameters to vary spatially by partitioning the domain into cells, ranking candidate partitions by a penalized-likelihood criterion, and averaging an ensemble of fitted models over locations.
DOMAIN: seismology
STRUCTURE: other: self-exciting point process
DATA_OBJECT: point set
INFERENCE: frequentist point estimate
PROBLEM_FORM: estimation
DISTRIBUTION: count; conditional-intensity point process
COMPLEXITY: polynomial iterative
DATA_AVAILABILITY: public-benchmark-used
CODE_AVAILABILITY: none
PREREGISTRATION: none
EVIDENCE_BASIS: empirical-with-released-data
