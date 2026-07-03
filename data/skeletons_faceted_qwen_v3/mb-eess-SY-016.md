MECHANISM: The paper computes a dynamic optimization framework that jointly models lane-change decisions and routing for entities in a network with constrained resources. It begins by predicting inflow rates on discrete segments using time-indexed observations of entity positions and speeds, estimating travel times via a parametric function. A bus-protection mechanism identifies segments where interference might occur by defining a time window around predicted bus arrivals and calculating conflict inflow rates. The framework then enforces hard constraints to prevent entities from entering protected segments during these windows. For eligible entities, a utility function combines three factors: normalized travel time savings from lane changes, feasibility of downstream routing, and penalties for frequent maneuvers. The utility is maximized per segment to select a single entity for a lane change, ensuring no conflicts. If bus travel time on a protected segment exceeds a threshold, the controller evaluates adjacent segments and reroutes entities to mitigate delays. The process iterates over time steps, updating predictions and constraints based on real-time observations. All computations are deterministic, relying on pre-defined parameters and observed states rather than probabilistic models. The method explicitly couples network-level routing with segment-level control to prevent congestion before it forms, using a combination of predictive analytics and constraint enforcement.  
DOMAIN: intelligent transportation systems  
STRUCTURE: other: predictive optimization  
DATA_OBJECT: graph or network  
INFERENCE: deterministic or closed-form  
PROBLEM_FORM: optimization  
DISTRIBUTION: none  
COMPLEXITY: not stated  
DATA_AVAILABILITY: public-benchmark-used  
CODE_AVAILABILITY: none  
PREREGISTRATION: none  
EVIDENCE_BASIS: simulation-study
