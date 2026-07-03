MECHANISM: Generates parametric probability distributions for particle shower Cherenkov light yield in ice/water. Use FLUKA Monte Carlo to simulate primary particles (p, n, π, K, Λ, Σ, Ξ, Ω, e, γ) at energies 10 GeV–1 PeV in ice; track all secondaries; compute weighted track length (Frank-Tamm corrected) along shower axis. Fit gamma distributions to individual shower profiles; model shape parameters (a, b) via basis splines in (a', b', E) space using penalized GLM; model amplitude (total weighted track length) via skew-normal (hadrons) or normal-inverse-Gaussian (EM) distributions with polynomial energy dependence. Sample from distributions to produce fluctuating shower profiles.
DOMAIN: Particle simulation, neutrino telescope signal modeling
STRUCTURE: sparse linear algebra (basis spline fitting)
DATA_OBJECT: sequence or time-series (shower profile along axis)
INFERENCE: variational
PROBLEM_FORM: simulation or generation
DISTRIBUTION: continuous; parametrized as gamma (shape/rate), skew-normal or NIG (amplitude)
COMPLEXITY: polynomial iterative
