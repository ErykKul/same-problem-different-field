MECHANISM: The paper computes a conditional p-threshold mutual information (MI) based Minimum Spanning Tree (MST) network framework to analyze financial market dependencies. First, it identifies crash periods using the Hellinger distance (HD), which quantifies abrupt shifts in the cross-sectional distribution of returns. The HD is calculated by comparing a reference distribution from a rolling window of past returns to the current distribution, with a threshold defined as the mean plus twice the standard deviation of the HD series. Crash periods are then characterized using the Hilbert spectrum (HS), which provides a time-frequency-energy analysis of volatility. Next, market-adjusted abnormal returns are computed by regressing stock returns on a market index using the Capital Asset Pricing Model (CAPM), isolating idiosyncratic components. Mutual information (MI) is estimated between pairs of abnormal returns using histogram-based density estimation, capturing both linear and nonlinear dependencies. Permutation-based significance testing is applied to retain only statistically significant MI values, filtering out spurious correlations. The resulting MI matrix is thresholded using a conditional p-value approach, where edges are included if their MI exceeds a significance threshold derived from permutation tests. The thresholded MI matrix is then used to construct MST networks, which are sparse, connected graphs representing the most significant dependencies. Network metrics such as core concentration, periphery fragility, centrality distributions, and modularity are computed to quantify structural reconfiguration and systemic vulnerability across pre-crash, crash, and post-crash periods. The analysis reveals changes in core-periphery structure, including reduced core concentration and increased periphery fragility during crashes, supported by disassortative mixing patterns. Post-crash networks show partial recovery, with persistent structural effects validated using the Gutenberg–Richter law to analyze aftershocks.  
DOMAIN: financial networks  
STRUCTURE: other: network construction  
DATA_OBJECT: graph or network  
INFERENCE: bootstrap or resampling  
PROBLEM_FORM: estimation  
DISTRIBUTION: none  
COMPLEXITY: not stated  
DATA_AVAILABILITY: public-benchmark-used  
CODE_AVAILABILITY: none  
PREREGISTRATION: none  
EVIDENCE_BASIS: empirical-with-private-data
