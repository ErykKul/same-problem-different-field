MECHANISM: Each entity is a finite sequence of discrete tokens drawn from a large alphabet. A reference table maps each token type to a scalar weight, and tokens are bucketed into a set of bins according to thresholds on that weight (linear, multiplicative, or logarithmic bin edges). Each token instance is assigned a normalized position equal to its index divided by sequence length. For each bin, the gaps between consecutive normalized positions of its member tokens are formed, including boundary gaps at the start and end. For each bin two summary statistics are computed: the mean gap and the variance of gaps. These per-bin statistics are concatenated into a fixed-length real feature vector that represents the sequence. Labeled feature vectors are then used to train a supervised margin-based classifier that assigns a query sequence to one of a finite candidate set. An extended scheme splits a long query into many sub-sequences, classifies each, computes the proportion assigned to each candidate, and forms a confidence score by comparing that proportion against the uniform baseline; the query is assigned to a candidate only if exactly one confidence exceeds a threshold, else it is rejected.
DOMAIN: authorship attribution, stylometry, digital humanities
STRUCTURE: kernel method
DATA_OBJECT: sequence or time-series
INFERENCE: deterministic optimization
PROBLEM_FORM: prediction or classification
DISTRIBUTION: count; nonparametric
COMPLEXITY: not stated
