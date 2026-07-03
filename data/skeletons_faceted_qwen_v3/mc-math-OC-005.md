MECHANISM: The paper computes a near-optimal control policy for a nonlinear system with parametric uncertainty by integrating adaptive dynamic programming (ADP) with barrier-state (BaS) augmentation. The method begins by defining a barrier function that transforms safety constraints into a bounded state variable, embedding safety directly into the system dynamics. A value function is optimized to penalize deviations from the barrier state, ensuring safety through the Bellman equation structure. The control policy is derived using model-based reinforcement learning, which is combined with a concurrent learning estimator to identify unknown parameters. The estimator uses a history stack of delayed samples to maintain sufficient excitation for parameter convergence without requiring persistent excitation. A Lyapunov-based analysis proves boundedness of the barrier dynamics and closed-loop stability. The augmented system state includes the barrier state, and the control law minimizes a quadratic cost functional that balances safety, stability, and performance. The parameter estimation error dynamics are governed by a time-varying gain matrix that adapts based on regressor matrix properties. The method ensures uniform convergence of parameter estimates and guarantees safety through forward-invariant constraints encoded in the barrier state.  
DOMAIN: control theory and adaptive systems  
STRUCTURE: dynamic programming  
DATA_OBJECT: state vector and parameter vector  
INFERENCE: deterministic or closed-form  
PROBLEM_FORM: control or optimization  
DISTRIBUTION: none  
COMPLEXITY: polynomial iterative  
DATA_AVAILABILITY: none  
CODE_AVAILABILITY: none  
PREREGISTRATION: none  
EVIDENCE_BASIS: simulation-study
