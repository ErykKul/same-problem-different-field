MECHANISM: Record time-series signals from a multielectrode array sampling at high frequency. Apply a high-pass filter to suppress noise and detect spikes as instances where signal amplitude exceeds a threshold. Segment the detected spike sequences into fixed-length windows. Train two neural networks jointly: a generator that synthesizes fake spike windows from random noise, and a discriminator that classifies real spike windows into categories while distinguishing synthetic samples. Use the discriminator as the classifier, trained on a small labeled subset and large unlabeled subset via semi-supervised adversarial learning.
DOMAIN: Neural spike classification using generative adversarial networks
STRUCTURE: other: adversarial training
DATA_OBJECT: sequence or time-series
INFERENCE: optimization only
PROBLEM_FORM: prediction or classification
DISTRIBUTION: ordinal; ordinal
COMPLEXITY: not stated
