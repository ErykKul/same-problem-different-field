MECHANISM: Time-ordered snapshots of several scalar and vector fields sampled on a uniform three-dimensional grid are processed to estimate a derived dimensionless parameter and track its evolution. A region of interest is selected by masking cells whose temperature falls outside a fixed band, leaving a near-uniform subpopulation. Each field is separated into systematic and fluctuating parts by applying a Gaussian low-pass convolution at a fixed characteristic scale and subtracting the smoothed field from the original; missing cells are handled by a renormalized weighting that ignores them. From the fluctuating density the standard deviation of the normalized field is computed, working in logarithm to tame the dynamic range and then mapping back. The fluctuating velocity components yield per-axis dispersions whose quadrature sum gives a dimensionless intensity, and the fluctuating vector field yields a pressure-like ratio through a closed algebraic expression. These three statistics are combined through a fixed analytic relation to invert for the target parameter at each snapshot. Finally, the target parameter and the auxiliary statistics are correlated against a separately tracked activity rate using a rank correlation coefficient with significance values, and lead-lag structure across snapshots is examined for delayed associations.
DOMAIN: interstellar medium turbulence in galaxy simulations
STRUCTURE: structured grid
DATA_OBJECT: grid or lattice
INFERENCE: frequentist point estimate
PROBLEM_FORM: estimation
DISTRIBUTION: continuous; gaussian
COMPLEXITY: closed-form
