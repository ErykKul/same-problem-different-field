MECHANISM: The paper computes a stochastic susceptible–infected–susceptible (SIS) model on hypergraphs, distinguishing between two transmission modes. Nodes represent entities with binary states (infected or susceptible), and hyperedges (group interactions) have binary states (contaminated or uncontaminated). Transmission occurs via two mechanisms: one through pairwise interactions (edges) and another through group interactions (hyperedges of size ≥3). Transition rates depend on parameters β_d (droplet transmission), β_e (aerosol transmission), γ (node recovery), σ (environmental contamination), and δ (hyperedge recovery). The model derives mean-field approximations by replacing stochastic variables with their expected values, leading to ordinary differential equations (ODEs) for node and hyperedge states. Threshold conditions for disease persistence are derived as R₀ = β_d(N−1)/γ + β_eσg′(0)C(N−1,s−1)s/(γδ), where C is a combinatorial coefficient. Simulations test how hyperedge size distributions and recovery rates affect disease dynamics, including comparisons between uniform and nonuniform hyperedge structures. The model also incorporates a sigmoid function g to quantify environmental contamination risk based on infected node counts within hyperedges.  
DOMAIN: epidemiology and network science  
STRUCTURE: other: mean-field approximation  
DATA_OBJECT: graph or network  
INFERENCE: deterministic or closed-form  
PROBLEM_FORM: simulation or generation  
DISTRIBUTION: none  
COMPLEXITY: not stated  
DATA_AVAILABILITY: public-repository  
CODE_AVAILABILITY: public-repository  
PREREGISTRATION: none  
EVIDENCE_BASIS: empirical-with-released-data
