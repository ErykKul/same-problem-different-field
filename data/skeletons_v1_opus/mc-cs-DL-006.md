MECHANISM: The paper is primarily a procedural framework proposal augmenting a manual review workflow with an automated assistant, and most of it is qualitative guidance with no method of its own. Its single quantitative component is a pre-screening filter. A short statement of intent is composed and each candidate text record is encoded as a fixed-length vector by a pretrained encoder. A scalar similarity between the intent vector and each record vector is computed as the normalized inner product. The empirical distribution of these scalar scores over all records is formed as a histogram. This distribution is modeled as a weighted sum of two latent component densities, one for highly relevant and one for weakly relevant items, with nonnegative weights summing to one. The component means, variances, and mixing weights are fit to the observed scores. Decision boundaries are then placed using a simple statistical rule, either fixed standard-deviation offsets from the component means or quantile cutpoints. Records below the lower cut are discarded, records above the upper cut are routed to manual handling, and the middle band is routed to automated handling. The counts in each band are reported. No further computation is performed; the rest of the contribution is checklist and reporting guidance.
DOMAIN: research methodology, evidence synthesis
STRUCTURE: graphical models
DATA_OBJECT: set or table
INFERENCE: maximum likelihood
PROBLEM_FORM: decision or test
DISTRIBUTION: proportion or bounded; gaussian mixture
COMPLEXITY: polynomial iterative
