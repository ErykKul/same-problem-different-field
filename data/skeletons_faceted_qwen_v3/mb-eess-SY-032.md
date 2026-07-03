MECHANISM: The paper computes a joint estimation of dynamic origin-destination (O-D) demand and choice models using a computational graph-based approach. The process begins by defining a nested logit structure to model hierarchical mode/route choices, incorporating alternative-specific and zone-specific variables into a generalized disutility function. System-level data, including traffic counts, transit ridership, and travel times, are integrated to calibrate the model. The disutility function combines travel time, waiting time, monetary costs, and sociodemographic factors (e.g., income, population density) across different modes (car, bus, metro, park-and-ride). A computational graph is constructed to represent the multi-modal network, enabling dynamic traffic simulation and parameter estimation. The graph-based learning approach minimizes discrepancies between simulated outcomes (dynamic link flow, travel times, boarding/alighting counts) and observed data through iterative optimization. Hypothesis testing is performed using a Wald-based framework to assess parameter significance, leveraging the computational graph's structure to handle non-closed-form dynamics and high-dimensional variables. The method accommodates multi-source data with missing entries and scales to large networks by decomposing the problem into subgraphs. The estimation process involves solving a non-linear optimization problem with constraints derived from the nested logit model, while the hypothesis tests evaluate statistical significance of disutility parameters and zone-specific factors. The framework is designed to handle dynamic congestion effects and inter-modal dependencies through time-varying link performance functions and path-specific cost calculations.  
DOMAIN: transportation modeling, multi-modal systems  
STRUCTURE: other: computational graph  
DATA_OBJECT: graph or network; tensor  
INFERENCE: Bayesian posterior  
PROBLEM_FORM: estimation  
DISTRIBUTION: count; continuous; normal  
COMPLEXITY: not stated  
DATA_AVAILABILITY: public-benchmark-used  
CODE_AVAILABILITY: none  
PREREGISTRATION: none  
EVIDENCE_BASIS: empirical-with-released-data
