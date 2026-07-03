MECHANISM: The paper computes a weighted least squares error estimation of operand flows within a hetero-functional graph framework. It begins by defining a reference architecture that categorizes system elements into resources, processes, and operands. Resources enable processes, which transform or transport operands. The system is represented as a Petri net with places (buffers) and transitions (capabilities), connected by incidence tensors that encode flow relationships. A negative third-order hetero-functional incidence tensor tracks operand removal from buffers, while a positive tensor tracks injection. These tensors are matricized into second-order matrices to form an engineering system net. The state transition function updates buffer contents and capability states over discrete time steps using input and output firing vectors, scaled by the simulation time step. The WLSEHFGSE extends this by incorporating estimation error terms into state transition constraints, enabling inference of unknown flows from real-world data while preserving physical feasibility. The method uses a generic optimization framework to solve for operand flows, minimizing weighted squared errors between observed and predicted measurements. The framework integrates exogenous data through a measurement function that quantifies nutrient flows, aligning with the assumptions of the CAST model. The approach ensures structural consistency by embedding delivery and BMP effects within the graph-theoretic representation, restoring upstream-downstream connectivity and enabling cross-scale analysis.  
DOMAIN: environmental systems modeling  
STRUCTURE: other: optimization-based framework  
DATA_OBJECT: graph or network  
INFERENCE: deterministic or closed-form  
PROBLEM_FORM: estimation  
DISTRIBUTION: none  
COMPLEXITY: not stated  
DATA_AVAILABILITY: public-benchmark-used  
CODE_AVAILABILITY: none  
PREREGISTRATION: none  
EVIDENCE_BASIS: empirical-with-released-data
