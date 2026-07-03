MECHANISM: The paper computes a probabilistic estimate of encountering new entities in a trajectory of observations. Given a sequence of entities, it first sub-samples the trajectory to ensure independence between consecutive observations. For each sampled entity, it calculates the maximum distance (RMSD) to all other entities in the trajectory. These maximum distances are sorted in descending order, and each is mapped to a probability value P = i/N, where i is the rank in the sorted list and N is the total number of entities. This generates a curve of P versus distance, quantifying the likelihood of observing new structures as a function of distance threshold. The method avoids storing the full distance matrix by processing each entity's distances independently, storing only the maximum per entity. The sub-sampling factor is determined by identifying the time interval where maximum distances stabilize, ensuring uncorrelated observations. The algorithm iteratively refines this factor by analyzing distance trends across increasing time intervals. The final probability curve is derived from the sorted maximum distances and their corresponding ranks. This approach reduces memory usage from quadratic to linear in the number of entities while preserving the statistical properties of the original Good-Turing method.  
DOMAIN: molecular dynamics simulation  
STRUCTURE: other: distance-based processing  
DATA_OBJECT: sequence or time-series  
INFERENCE: deterministic or closed-form  
PROBLEM_FORM: estimation  
DISTRIBUTION: none  
COMPLEXITY: polynomial iterative  
DATA_AVAILABILITY: public-repository  
CODE_AVAILABILITY: public-repository  
PREREGISTRATION: none  
EVIDENCE_BASIS: empirical-with-released-data
