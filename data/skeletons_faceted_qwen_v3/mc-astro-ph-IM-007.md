MECHANISM: The paper computes parametric probability distributions to model the Cherenkov light yield from particle showers. It begins by simulating particle showers using Monte Carlo methods, which generate weighted track lengths and Cherenkov photon emission profiles. These simulations are used to derive empirical distributions of parameters that describe the shower's total light yield and its spatial profile. The model assumes a gamma distribution for the light yield as a function of distance along the shower axis, with parameters determined by non-linear least squares regression. To capture variations in the shape parameters of the gamma distribution, the paper employs basis splines and penalized B-splines to construct a joint probability density function over the transformed parameters. This density function is estimated using a tensor product of splines, with a penalized likelihood approach to avoid overfitting. The model is validated by comparing simulated and fitted distributions, and outliers are removed based on quantile thresholds and Wasserstein distances. The final model allows for fast approximations of the Cherenkov light yield and its fluctuations, which are critical for neutrino telescope simulations. The computational steps include simulation, parametric fitting, spline-based density estimation, and outlier removal. The method does not involve explicit optimization for a specific objective function but instead relies on statistical modeling of the simulated data.

DOMAIN: high-energy physics

STRUCTURE: simulation or generation

DATA_OBJECT: set or table

INFERENCE: optimization only

PROBLEM_FORM: simulation or generation

DISTRIBUTION: continuous; gamma

COMPLEXITY: not stated

DATA_AVAILABILITY: none

CODE_AVAILABILITY: none

PREREGISTRATION: none

EVIDENCE_BASIS: simulation-study
