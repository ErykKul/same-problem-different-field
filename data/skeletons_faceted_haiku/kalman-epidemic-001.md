MECHANISM: A dynamical system models the temporal evolution of latent quantities, governed by equations with unknown parameters. Observations of an aggregate quantity arrive sequentially in time. An ensemble of system realizations is propagated forward through the governing equations between observations. When an observation arrives, a recursive Bayesian update adjusts each ensemble member by its likelihood under a measurement model, producing a posterior ensemble over both the latent state and the parameters. The updated ensemble reinitializes the forward integration, and the integrate-then-update cycle repeats as further observations arrive. Forecasts are produced by integrating the posterior ensemble forward, and predictive confidence is read from the spread of the ensemble.
DOMAIN: epidemiology
STRUCTURE: other: sequential state-space estimation
DATA_OBJECT: sequence or time-series
INFERENCE: Bayesian posterior
PROBLEM_FORM: estimation
DISTRIBUTION: none
COMPLEXITY: polynomial iterative
DATA_AVAILABILITY: public-benchmark-used
CODE_AVAILABILITY: none
PREREGISTRATION: none
EVIDENCE_BASIS: empirical-with-released-data
