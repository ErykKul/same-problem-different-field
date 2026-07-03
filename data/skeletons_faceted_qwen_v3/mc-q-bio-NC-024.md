MECHANISM: The paper computes the effects of two distinct calcium current types on synchronized neural activity patterns in a network model. It begins by defining a conductance-based model for subthalamic nucleus (STN) and globus pallidus externus (GPe) neurons, incorporating voltage-gated ionic currents (including T-type and L-type calcium currents) and synaptic interactions. The model uses differential equations to describe membrane potential dynamics, gating variable kinetics, and calcium concentration changes. Network-level interactions are simulated through synaptic connections between STN and GPe neurons, with parameters modulating synaptic strength and external inputs. The study applies periodic external inputs to observe network responses, analyzes transitions between synchronized and desynchronized states using phase reconstruction and return maps, and quantifies synchronization via principal component analysis of slow variables. The computational steps include solving ordinary differential equations numerically, simulating network dynamics under varying parameter conditions, and extracting statistical features from the resulting time-series data to infer the role of calcium currents in shaping rhythmic activity. The analysis compares simulated patterns to empirical observations from Parkinsonian patients, focusing on how calcium currents influence burst duration, synchrony range, and resistance to external entrainment. The method does not involve probabilistic inference or optimization but relies on deterministic simulation of biophysically detailed models.  
DOMAIN: neuroscience  
STRUCTURE: other: differential equations  
DATA_OBJECT: graph or network  
INFERENCE: deterministic or closed-form  
PROBLEM_FORM: simulation or generation  
DISTRIBUTION: none  
COMPLEXITY: not stated  
DATA_AVAILABILITY: none  
CODE_AVAILABILITY: none  
PREREGISTRATION: none  
EVIDENCE_BASIS: simulation-study
