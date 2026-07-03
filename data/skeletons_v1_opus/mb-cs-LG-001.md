MECHANISM: Given an input formed by concatenating a query with a set of retrieved items, the system computes a binary decision that routes processing down one of two paths. A pretrained parameterized sequence model is adapted by adding a low-rank correction to its weight matrices, writing each weight as the original plus a product of two thin factors with rank far below the dimension. Only these factors are trained, minimizing the negative log-probability of a single target label token over a labeled dataset via gradient descent. At decision time, autoregressive generation is suppressed and a mask is applied to the output logits so that all probability mass is forced onto the two admissible label tokens, after which a single token is emitted. This reduces the decision cost to one forward pass over the input length. The emitted token selects either direct downstream generation or an interception that invokes an auxiliary retrieval action and re-runs generation with augmented context. Performance is measured by routing precision and recall, downstream faithfulness, latency, and per-query cost on inputs corrupted with adversarial distractors. An ablation contrasts the adapted model against its untuned form to quantify the reduction in false positives.
DOMAIN: retrieval-augmented language model routing
STRUCTURE: neural network
DATA_OBJECT: sequence or time-series
INFERENCE: maximum likelihood
PROBLEM_FORM: prediction or classification
DISTRIBUTION: binary; logistic
COMPLEXITY: not stated
