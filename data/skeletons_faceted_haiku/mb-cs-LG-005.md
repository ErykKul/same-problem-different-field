MECHANISM: A discrete flow matching model learns to approximate the posterior distribution of target sequences given intermediate noisy states through a neural network denoiser trained via cross-entropy loss. The flow operates along a probability path that smoothly interpolates from a source to a target distribution. For active generation, standard variational objectives are reformulated to operate on conditional endpoint distributions (which are tractable from the flow) rather than marginal likelihoods. Forward-KL and reverse-KL variants are derived using self-normalized importance sampling, with weights computed from a trained classifier estimating fitness probability. Sampling proceeds via iterative parallel refinement along the probability path, updating all sequence positions at each step conditioned on the full context.

DOMAIN: generative modeling, active learning, black-box optimization, discrete sequence design

STRUCTURE: other: parallel iterative refinement with neural denoiser

DATA_OBJECT: sequence or time-series

INFERENCE: variational

PROBLEM_FORM: optimization

DISTRIBUTION: discrete; discrete

COMPLEXITY: not stated
