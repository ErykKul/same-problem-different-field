MECHANISM: The paper computes exact solutions to a vehicle routing problem with time and energy constraints by constructing and comparing three mathematical formulations. The problem involves routing vehicles to serve customer pickups and deliveries while managing battery recharging. The formulations use event-based and fragment-based representations of routes, where events denote locations and customer states, and fragments represent partial paths with specific load conditions. The method introduces arc-flow variables to track battery state-of-charge (SoC) and incorporates constraints on pairing, precedence, capacity, time windows, and maximum ride time. Discretization of time and SoC is applied to reduce computational complexity, enabling the use of fragment-based methods. The formulations are evaluated through computational experiments to assess how discretization affects solution quality and efficiency. The core algorithm involves generating event arcs and fragment paths, enforcing constraints through network structure, and solving the resulting optimization problem using branch-and-price or similar exact methods. The comparison isolates the effects of time and SoC discretization by varying these parameters across formulations. The method does not rely on probabilistic inference or sampling but instead uses deterministic optimization to minimize a weighted cost function combining travel cost and customer ride time.  
DOMAIN: transportation logistics, vehicle routing, electric vehicle optimization  
STRUCTURE: branch-and-bound  
DATA_OBJECT: graph or network  
INFERENCE: deterministic or closed-form  
PROBLEM_FORM: optimization  
DISTRIBUTION: none  
COMPLEXITY: not stated  
DATA_AVAILABILITY: public-benchmark-used  
CODE_AVAILABILITY: none  
PREREGISTRATION: none  
EVIDENCE_BASIS: empirical-with-released-data
