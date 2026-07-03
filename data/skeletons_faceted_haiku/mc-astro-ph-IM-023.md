MECHANISM: A custom semianalytic orbit propagator integrates mean orbital elements under atmospheric drag and J2 perturbations using Gauss-Legendre quadrature and Runge-Kutta integration, with atmospheric density from NRLMSISE-00. Ballistic coefficient is extracted from TLE pairs using orbital momentum changes and averaged atmospheric density. These components feed a Monte Carlo ensemble that disperses the ballistic coefficient via log-uniform scaling factors. Predictions are scored against actual deorbit dates using empirical continuously ranked probability score (CRPS) and Cramér-von Mises criteria, across three validation scenarios: perfect knowledge, historical conditions, and fully predictive.
DOMAIN: Astrodynamics; orbit prediction; space operations
STRUCTURE: sparse linear algebra
DATA_OBJECT: time series or sequence
INFERENCE: Bayesian posterior
PROBLEM_FORM: prediction or classification
DISTRIBUTION: none
COMPLEXITY: not stated
