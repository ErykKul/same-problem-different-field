MECHANISM: The paper computes an optimal parking strategy using a dynamic programming framework that models the problem as an infinite-horizon Markov decision process (MDP). The state space includes the vehicle's location (origin or parking lot) and parking status (unparked or parked). Actions represent attempts to park at specific lots, with success probabilities determined by lot-specific availability. Rewards are defined as negative time costs, incorporating drive time, wait time, and walk time to the destination. The objective is to minimize the expected cumulative reward (equivalent to minimizing expected time-to-arrive). The framework derives closed-form expressions for optimal strategies under two regimes: (1) when driving to a single lot with the highest value-to-go, and (2) when cycling through a cluster of lots with lower inter-lot travel times than wait times. Sensitivity analysis quantifies conditions under which switching strategies remains optimal. The model also accommodates dynamic probabilities by analyzing how other vehicles' actions affect parking availability, leading to closed-form expressions for updated probabilities.  
DOMAIN: urban mobility and transportation planning  
STRUCTURE: dynamic programming  
DATA_OBJECT: set or table  
INFERENCE: deterministic or closed-form  
PROBLEM_FORM: optimization  
DISTRIBUTION: continuous; bounded  
COMPLEXITY: polynomial iterative  
DATA_AVAILABILITY: dataset-with-DOI-or-handle  
CODE_AVAILABILITY: none  
PREREGISTRATION: none  
EVIDENCE_BASIS: empirical-with-released-data
