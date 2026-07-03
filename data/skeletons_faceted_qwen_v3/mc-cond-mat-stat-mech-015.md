MECHANISM: The paper computes a critical threshold for volatility in a recursive model of rectified Gaussian expectations. It begins with a random variable X following a Gaussian distribution, applies a rectification operation (max(X, 0)), and computes the expected value of the rectified variable. This expectation is iteratively fed forward as the mean of subsequent Gaussian distributions, each with volatility σ. The recursion depends on a parameter α derived from σ and the previous iteration's output. The system exhibits a phase transition when α crosses a critical value, leading to either convergence or divergence of the iterated expectations. The critical threshold is derived analytically using properties of the Gaussian distribution and the inverse Mills ratio. When selective survival conditions are introduced (participants require minimum returns to continue), the threshold decreases, and the distribution of outcomes transitions to a power-law form. The power-law exponent is expressed in terms of survival pressure and conditional growth rates. The model is self-similar at the critical threshold, with each iteration reproducing the statistical structure of the previous one. The computation involves solving nonlinear recursions, evaluating integrals of Gaussian functions, and analyzing convergence behavior based on volatility and survival parameters. The result is a closed-form expression for the critical volatility and the power-law distribution of outcomes under supercritical conditions.  
DOMAIN: financial systems  
STRUCTURE: dynamic programming  
DATA_OBJECT: sequence or time-series  
INFERENCE: deterministic or closed-form  
PROBLEM_FORM: estimation  
DISTRIBUTION: power-law; gaussian  
COMPLEXITY: closed-form  
DATA_AVAILABILITY: none  
CODE_AVAILABILITY: none  
PREREGISTRATION: none  
EVIDENCE_BASIS: mathematical-proof
