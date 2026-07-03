MECHANISM: The paper describes a computational method for estimating time-varying parameters in statistical models using a discrete-valued latent stochastic process governed by a Markov property. The state indicator at each time step depends only on the previous state and a transition matrix defining state transition probabilities. The method involves filtering and smoothing techniques to estimate the probability distribution of state occurrences across time periods, as well as estimating regime-specific parameters. The model assumes a finite number of regimes with exogenous Markov processes, where state transitions are independent of model innovations. Extensions include allowing time-dependent transition probabilities via explanatory variables or functions of the state indicator, and Infinite Hidden Markov models that permit an unbounded number of states. The endogenous Markov switching model explicitly links the state indicator to model innovations, improving interpretability. Estimation procedures rely on probabilistic inference over sequences of states and parameters, with applications to forecasting and parameter interpretation under persistent regimes. The method does not explicitly name standard algorithms like Kalman filters but describes the underlying probabilistic structure and inference steps.  
DOMAIN: time-series econometrics  
STRUCTURE: graphical models  
DATA_OBJECT: sequence or time-series  
INFERENCE: Bayesian posterior  
PROBLEM_FORM: estimation  
DISTRIBUTION: continuous; Gaussian  
COMPLEXITY: not stated  
DATA_AVAILABILITY: none  
CODE_AVAILABILITY: none  
PREREGISTRATION: none  
EVIDENCE_BASIS: review-or-position
