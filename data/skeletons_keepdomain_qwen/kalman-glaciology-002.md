MECHANISM: The paper computes a parallel Ensemble Kalman Filter (EnKF) algorithm for ice sheet models, using a nonlinear, transformation-based update scheme that avoids explicit construction of the forecast error covariance matrix. The method operates on ensemble-based state and parameter estimates, applying a matrix-free formulation to maintain scalability in high-dimensional systems. Observations are assimilated into the model state through a hybrid assimilation–inversion strategy, where ensemble-based data assimilation corrects the state, and physics-based inverse methods infer unobserved parameters like basal friction. The algorithm supports both localized and non-localized variants, with the core EnKF variant using a parallel MPI implementation for distributed computation. The framework couples with existing ice sheet models via modular interfaces, enabling adaptive state indexing and efficient I/O. The method iteratively updates model states and parameters by transforming ensemble members using observation data, without requiring explicit covariance matrix localization. The paper demonstrates the framework's application to ISSM and Icepack models, showing joint state estimation and parameter inference through benchmark simulations on high-performance computing platforms. The computational steps include ensemble generation, forward simulation, observation assimilation, parameter inversion, and output aggregation for scalability.  
DOMAIN: ice sheet modeling and data assimilation  
STRUCTURE: map-reduce or embarrassingly-parallel  
DATA_OBJECT: high-dimensional state and parameter spaces  
INFERENCE: Bayesian posterior  
PROBLEM_FORM: estimation  
DISTRIBUTION: none  
COMPLEXITY: not stated  
DATA_AVAILABILITY: none  
CODE_AVAILABILITY: public-repository  
PREREGISTRATION: none  
EVIDENCE_BASIS: empirical-with-released-data
