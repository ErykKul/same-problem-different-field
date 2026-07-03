MECHANISM: A large corpus of short text items is partitioned into time windows and grouped into discovered categories, yielding for each window a distribution of item counts across categories. From this count distribution several scalar concentration indicators are computed: an inequality coefficient formed from the rank-weighted sum of sorted counts normalized by total mass, an entropy of the category proportions, and a parameterized single-peaked function of the category-to-item ratio. Closed-form limiting expressions for the inequality coefficient are derived under extreme allocations to show it distinguishes equal versus monopolized distributions that share the same ratio. In parallel, each item is assigned a discrete class by a learned classifier built on contextual embeddings, and the per-window fraction in the target class is recorded. Two aligned time series are thereby produced for each group: one of a concentration scalar and one of a class fraction. Their linear association is measured by the sample correlation coefficient, computed both by pooling all groups into a global series and separately within each group. The central output is the comparison of these correlation magnitudes across indicators and across the global-versus-local aggregation.
DOMAIN: social media information overload and misinformation
STRUCTURE: other: summary statistics and correlation
DATA_OBJECT: sequence or time-series
INFERENCE: frequentist point estimate
PROBLEM_FORM: estimation
DISTRIBUTION: count; none
COMPLEXITY: closed-form
