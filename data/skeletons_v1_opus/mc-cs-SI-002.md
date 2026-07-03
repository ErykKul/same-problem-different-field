MECHANISM: Each observation is a pair of short text items drawn from a thread structure, and the goal is to assign a scalar intensity to the pair and then aggregate. First, a large pretrained language model is queried with a fixed template, configured for deterministic output, to map each item-pair to a few categorical attributes: a discrete position label, a binary indicator of charged tone, and a discrete agreement label. Second, a fixed lookup table of hand-specified rules maps each combination of these categorical attributes to an integer score on a bounded scale. Third, the score for a group of pairs is computed as the arithmetic mean of its member scores. Finally, the mean score and its standard error are computed within each of several disjoint temporal windows around discrete events, and the windowed means are compared to detect when the quantity rises. The computational core is a deterministic categorical-to-score mapping followed by group averaging and across-group comparison; the classification step itself is delegated to an external model and is not derived here.
DOMAIN: online social media discourse analysis
STRUCTURE: other: rule-based lookup with aggregation
DATA_OBJECT: set or table
INFERENCE: deterministic or closed-form
PROBLEM_FORM: prediction or classification
DISTRIBUTION: ordinal; none
COMPLEXITY: closed-form
