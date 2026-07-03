MECHANISM: Formulate parking location selection as an infinite-horizon Markov decision process. States represent current location and parking status (parked or unparked). At each step an agent chooses a parking lot to visit, succeeding with known probability and incurring travel time plus potential waiting time. If unsuccessful, the agent can either wait at the current lot (retrying with exponential waiting cost) or drive to a different lot. Dynamic programming solves for optimal policy and expected cost. Closed-form expressions characterize two regimes: patient strategies (stay at best lot) and exploratory strategies (visit a cluster of nearby lots).
DOMAIN: Parking and urban transportation planning
STRUCTURE: dynamic programming
DATA_OBJECT: graph or network
INFERENCE: frequentist point estimate
PROBLEM_FORM: optimization
DISTRIBUTION: none
COMPLEXITY: closed-form
