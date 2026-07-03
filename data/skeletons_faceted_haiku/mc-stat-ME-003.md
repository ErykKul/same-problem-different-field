MECHANISM: Constructs rank-based score matrices via pairwise comparisons between observations; centers score matrices to remove marginal effects; performs Whitney embedding by summing row terms to transform into Euclidean space on Riemannian manifold (Kemeny metric); computes sample correlation as ratio of cross-moment to product of standard deviations; formulates quasi-likelihood function combining multiple central moments (second, third, fourth) with learned weights; derives moment-weighted loss function minimized over moment weights; computes Fisher information matrix from second derivatives of log-likelihood; establishes exact unbiasedness via U-statistic theory and exchangeability; proves finite-sample efficiency at Cramer-Rao bound through Hajek projection.
DOMAIN: Semi-parametric rank-based correlation estimation with moment-based quasi-likelihood
STRUCTURE: combinational logic
DATA_OBJECT: dense matrix or tensor
INFERENCE: frequentist point estimate
PROBLEM_FORM: estimation
DISTRIBUTION: continuous; continuous
COMPLEXITY: polynomial iterative
