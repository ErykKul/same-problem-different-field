MECHANISM: The paper computes a stimulus-dependent maximum entropy (SDME) model to estimate the conditional probability distribution over neural codewords given sensory input. The model extends the linear-nonlinear model of single neurons to a pairwise-coupled population by incorporating interactions between neurons. It maximizes entropy subject to constraints derived from observed data, including single-cell response statistics and pairwise correlations. Parameters are estimated using maximum likelihood or similar optimization techniques to match empirical moments of the data. The model explicitly accounts for dependencies between neurons through pairwise coupling terms, which capture both shared stimulus effects and direct neuron-to-neuron interactions. The method is applied to retinal ganglion cell recordings under temporal white-noise stimuli, where it outperforms uncoupled models in reproducing codeword distributions. The SDME model's structure includes both individual neuron response properties and higher-order interactions, which are critical for encoding stimulus information. The computational steps involve defining the entropy-maximizing distribution, fitting parameters to match observed statistics, and validating the model's accuracy against empirical data. The approach is domain-specific, relying on the structure of neural populations and their response to stimuli. The model's parameters are inferred from large-scale recordings, and its performance is evaluated using statistical measures of codeword distribution accuracy. The method does not rely on sampling or Bayesian inference but instead uses deterministic optimization to find the best-fitting distribution.

DOMAIN: neuroscience

STRUCTURE: graphical models

DATA_OBJECT: sequence or time-series

INFERENCE: optimization only

PROBLEM_FORM: estimation

DISTRIBUTION: binary; binary

COMPLEXITY: not stated

DATA_AVAILABILITY: none

CODE_AVAILABILITY: none

PREREGISTRATION: none

EVIDENCE_BASIS: empirical-with-private-data
