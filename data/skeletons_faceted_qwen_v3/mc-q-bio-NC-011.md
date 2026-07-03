MECHANISM: The paper computes the robustness of dynamical regimes under parametric uncertainty by modeling the system as a stochastic process with parameters drawn from a uniform distribution. It uses generalized polynomial chaos (gPC) to approximate the stochastic process, expanding the state variables in terms of orthogonal polynomials corresponding to the parameter distribution. This expansion allows the computation of the mean state trajectory as a deterministic function of time, incorporating uncertainty effects analytically. The mean trajectory is then analyzed using recurrence plots, where geometric patterns (specifically blob counts) are extracted to quantify regime preservation. Blob counts are derived from the recurrence plots by identifying and counting distinct regions of recurrence, which are compared across parameter variations to assess robustness. The method combines the gPC approximation with recurrence analysis to map parameter spaces where the nominal regime is preserved in expectation. The result is a probabilistic regime preservation (PRP) plot that visualizes the relationship between parameter uncertainty and regime robustness. The approach systematically evaluates how deviations from nominal parameter values affect the mean signal's recurrence structure, distinguishing between parameter regions that maintain the regime and those that do not. The method does not rely on sampling or Monte Carlo techniques but instead uses polynomial expansions to capture uncertainty propagation. The final output is a quantitative measure of robustness, expressed as the maximum allowable parameter deviation that preserves the regime in expectation.  
DOMAIN: neuroscience  
STRUCTURE: spectral or transform  
DATA_OBJECT: continuous function or field  
INFERENCE: deterministic or closed-form  
PROBLEM_FORM: estimation  
DISTRIBUTION: continuous; uniform  
COMPLEXITY: not stated  
DATA_AVAILABILITY: none  
CODE_AVAILABILITY: none  
PREREGISTRATION: none  
EVIDENCE_BASIS: simulation-study
