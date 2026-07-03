MECHANISM: The paper computes a multi-dimensional opinion dynamics model where entities are characterized by a vector of quantities and a weighting factor across these quantities. Opinions evolve through binary interactions, with changes in one quantity depending on the weighted similarity across the full vector. The model defines a distance metric combining direct differences and weighted sums of differences across all quantities. Binary interactions are governed by a non-increasing interaction function applied component-wise to the distance metric. Post-interaction states are computed by adjusting each quantity based on the interaction function's value and the difference between pre-interaction states. The kinetic equation for the process is derived, leading to a mean-field partial differential equation describing the distribution of entities over time. The model ensures opinions remain within bounded intervals through the interaction rules. Analytical and numerical methods confirm the emergence of complex stationary states, dependent on the weighting factors. The existence and properties of solutions are analyzed, showing conservation of mass and non-negativity preservation. The model generalizes classical consensus formation by incorporating multi-dimensional interactions and weighted importance across quantities.  
DOMAIN: social science modeling  
STRUCTURE: other: partial differential equation  
DATA_OBJECT: continuous function or field  
INFERENCE: none  
PROBLEM_FORM: simulation or generation  
DISTRIBUTION: none  
COMPLEXITY: not stated  
DATA_AVAILABILITY: none  
CODE_AVAILABILITY: none  
PREREGISTRATION: none  
EVIDENCE_BASIS: simulation-study
