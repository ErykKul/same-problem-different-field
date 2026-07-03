MECHANISM: The paper computes a decentralized optimization process where agents interact with a shared environment to minimize expected traversal time. Agents are modeled as self-propelled particles with position and orientation, governed by stochastic differential equations that include both trail-following and trail-optimizing control inputs. The pheromone field, a continuous spatiotemporal function, evolves via a reaction-diffusion equation, coupling agent behavior and environmental modification. The control law for trail-following is derived from gradient descent on the K-L divergence between agent density and pheromone concentration, aligning agent headings with pheromone gradients. Trail optimization involves solving a stochastic control problem using adjoint methods, minimizing a functional that combines traversal time and control effort. The solution yields a feedback law for steering, determined by adjoint sensitivities that encode geometric path optimization. The process iterates between forward agent traversal and backward pheromone reinforcement, leading to emergent geodesic paths. The mathematical framework connects this to eikonal geometry, showing that stigmergic dynamics approximate Fermat’s principle through local interactions without global knowledge.  
DOMAIN: stochastic optimal control  
STRUCTURE: dynamic programming  
DATA_OBJECT: continuous function or field  
INFERENCE: optimization only  
PROBLEM_FORM: optimization  
DISTRIBUTION: none  
COMPLEXITY: not stated  
DATA_AVAILABILITY: public-repository  
CODE_AVAILABILITY: public-repository  
PREREGISTRATION: none  
EVIDENCE_BASIS: simulation-study
