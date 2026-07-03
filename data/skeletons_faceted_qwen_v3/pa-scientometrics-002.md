MECHANISM: The paper computes nonparametric estimates of preferential attachment functions and author fitnesses in temporal networks. It models the growth of co-authorship and citation networks by analyzing how node fitness and preferential attachment influence the addition of new edges over time. The method first constructs undirected co-authorship networks and directed citation networks from document metadata, then applies statistical algorithms to estimate attachment exponents and fitness distributions. It identifies heavy-tailed distributions of author fitness, inferring that intrinsic quality significantly affects citation and collaboration rates. The algorithm compares attachment exponents across network types, revealing weak rich-get-richer effects. It also tracks how competitiveness increases over time, affecting new edge acquisition. Fitness is modeled as a proxy for scientific quality, with higher fitness enabling nodes to gain edges even without prior connectivity. The method uses time-resolved network partitions to detect dynamic patterns, comparing results across four temporal intervals. It relies on disambiguated author identifiers and citation counts to build network structures, then applies mathematical models to infer parameters governing network evolution. The process involves detecting whether growth follows preferential attachment, fitness-driven mechanisms, or combinations, and quantifying their relative contributions through statistical estimation.  
DOMAIN: scientometrics  
STRUCTURE: other: network analysis  
DATA_OBJECT: graph or network  
INFERENCE: frequentist point estimate  
PROBLEM_FORM: estimation  
DISTRIBUTION: count; power-law  
COMPLEXITY: not stated  
DATA_AVAILABILITY: public-benchmark-used  
CODE_AVAILABILITY: none  
PREREGISTRATION: none  
EVIDENCE_BASIS: empirical-with-released-data
