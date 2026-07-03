MECHANISM: The paper computes a generative adversarial network (GAN) with additional structural constraints to preserve financial stylized facts. The generator maps latent noise to synthetic return series, while the discriminator distinguishes synthetic from real returns. A Wasserstein GAN with gradient penalty (WGAN-GP) loss is used for training stability. Four differentiable constraints enforce alignment with stylized facts: (i) generalized Pareto distribution (GPD) tail index minimization to capture heavy tails, (ii) mean squared error between autocorrelation functions of squared returns to model volatility clustering, (iii) correlation minimization between past returns and future volatility to enforce leverage effects, and (iv) Frobenius norm minimization between cross-scale volatility correlation matrices to preserve hierarchical dependencies. The generator's total loss combines adversarial loss with weighted sums of these constraints. The alignment module is model-agnostic and can be applied to various generator architectures. Training involves iterative optimization of generator and discriminator parameters, with gradual annealing of structural constraints to stabilize early dynamics. The method ensures generated series align with real market statistics beyond marginal distributions, enabling robust backtesting performance.  
DOMAIN: financial time series generation  
STRUCTURE: other: generative adversarial network  
DATA_OBJECT: sequence or time-series  
INFERENCE: deterministic or closed-form  
PROBLEM_FORM: simulation or generation  
DISTRIBUTION: none  
COMPLEXITY: not stated  
DATA_AVAILABILITY: public-benchmark-used  
CODE_AVAILABILITY: none  
PREREGISTRATION: none  
EVIDENCE_BASIS: empirical-with-private-data
