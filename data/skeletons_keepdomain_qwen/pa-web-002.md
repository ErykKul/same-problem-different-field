MECHANISM: The paper computes the preferential attachment exponent β by analyzing forty-seven longitudinal Web network datasets. It measures the degree distribution of nodes over time, fits a nonlinear preferential attachment model to the data, and estimates β as the exponent governing the relationship between node degree and attachment probability. The method involves aggregating temporal network data, calculating cumulative degree growth for each node, and applying regression or curve-fitting techniques to determine the exponent β for each network category. The analysis distinguishes between sublinear (β < 1), linear (β = 1), and superlinear (β > 1) attachment patterns across directed, undirected, and bipartite networks. The paper then correlates β values with network characteristics such as node heterogeneity, link formation dynamics, and external factors like user behavior or platform policies. It validates the model by comparing empirical β estimates against theoretical predictions and demonstrates that β varies systematically across network types. The computation does not involve simulation or optimization but focuses on statistical estimation of β from observed network growth patterns. The results are used to propose explanations for β variation based on network-specific mechanisms, such as homophily, external influence, or resource allocation rules. The method is applied to both static snapshots and time-evolving network data, with β computed as a summary statistic for each dataset. The paper emphasizes that β serves as a discriminative measure for network classification and a tool for understanding structural evolution in online systems.

DOMAIN: network analysis and web science

STRUCTURE: other: statistical analysis

DATA_OBJECT: graph or network

INFERENCE: frequentist point estimate

PROBLEM_FORM: estimation

DISTRIBUTION: none

COMPLEXITY: not stated

DATA_AVAILABILITY: public-benchmark-used

CODE_AVAILABILITY: none

PREREGISTRATION: none

EVIDENCE_BASIS: empirical-with-released-data
