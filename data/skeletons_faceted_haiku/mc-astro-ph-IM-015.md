MECHANISM: A training dataset of 995 synthetic stellar spectra is generated from non-LTE radiative transfer simulations (FASTWIND) with parameters sampled via Latin-hypercube design. Each spectrum is compressed via principal component analysis to 45 components explaining 99.3% of variance. For each principal component, a Gaussian-process emulator is trained to map stellar parameters to PC coefficients. These emulators are then coupled with Markov Chain Monte Carlo sampling to perform Bayesian inference of stellar parameters from observed spectra, with uncertainty quantification via posterior distributions.
DOMAIN: Stellar astrophysics; quantitative spectroscopy; machine learning for observational inference
STRUCTURE: dense linear algebra
DATA_OBJECT: dense matrix or tensor
INFERENCE: Bayesian posterior
PROBLEM_FORM: estimation
DISTRIBUTION: none
COMPLEXITY: not stated
