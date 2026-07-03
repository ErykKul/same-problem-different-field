MECHANISM: The paper computes a decision-making process involving a latent state that evolves over time, modeled as a Partially Observable Markov Decision Process (POMDP). The latent state represents an unobserved quantity that influences the system's behavior, transitioning based on actions taken by an agent. Observations are conditionally dependent on the interaction mode and the latent state, with some modes producing no observations. The model defines a reward function that combines immediate costs of actions (e.g., helping or signaling) with long-term benefits tied to the latent state. The transition and observation dynamics are estimated using an Expectation-Maximization (EM) algorithm applied to partially observable action-observation sequences. In the E-step, forward-backward probabilities are computed to infer expected state occupancies and transitions, while the M-step updates parameters by maximizing the likelihood of the observed data. The planning phase involves solving a Bellman equation in belief space, where the agent selects actions to maximize the expected cumulative discounted reward, balancing immediate outcomes with the long-term impact on the latent state. The belief state is recursively updated using the POMDP belief-update rule, incorporating observed outcomes and uncertainty about the latent state. The framework explicitly accounts for structured, mode-dependent observability and action-dependent costs, enabling the agent to influence the latent state over repeated interactions.  
DOMAIN: human-robot interaction and prosocial behavior modeling  
STRUCTURE: graphical models  
DATA_OBJECT: set or table  
INFERENCE: frequentist point estimate  
PROBLEM_FORM: control  
DISTRIBUTION: binary; Bernoulli  
COMPLEXITY: not stated  
DATA_AVAILABILITY: dataset-with-DOI-or-handle  
CODE_AVAILABILITY: none  
PREREGISTRATION: none  
EVIDENCE_BASIS: empirical-with-released-data
