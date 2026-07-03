MECHANISM: Partition all words in a text into frequency-based zones according to natural language frequency. Compute occurrence positions for each word and distances between consecutive occurrences within each zone. Calculate expectation and variance of inter-occurrence distances for each frequency zone. Concatenate these distribution features into a high-dimensional style vector. Apply support vector machine classification to discriminate between candidate authors using style feature vectors from training texts.
DOMAIN: Authorship attribution and computational stylometry
STRUCTURE: dense linear algebra
DATA_OBJECT: sequence or time-series
INFERENCE: deterministic or closed-form
PROBLEM_FORM: classification
DISTRIBUTION: none
COMPLEXITY: polynomial iterative
