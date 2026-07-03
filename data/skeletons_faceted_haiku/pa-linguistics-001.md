MECHANISM: A history-dependent stochastic model generates sequences (sentences) where the sample-space of available choices (words) progressively reduces as the sequence unfolds. At each step, an entity (word) is sampled uniformly from a restricted set (the words that can follow the previous entity), and this restricted set is derived from an empirical transition matrix capturing which entities can follow which others in observed data. The model produces a nested hierarchy of sample-spaces: each step constrains the next step's available choices. The algorithm repeatedly generates sequences and collects frequency statistics on the entities observed. The distribution of entity frequencies emerges as a power law when the sample-space reduction (measured by a nestedness parameter) is sufficiently strong, and breaks down when nestedness is weak.
DOMAIN: Linguistics and statistical language modeling
STRUCTURE: dynamic programming
DATA_OBJECT: sequence or time-series
INFERENCE: deterministic or closed-form
PROBLEM_FORM: estimation
DISTRIBUTION: none
COMPLEXITY: not stated
