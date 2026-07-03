MECHANISM: The paper computes three performance metrics—channel capacity, dynamic range, and effective Hill coefficient—for a probabilistic model of receptor cluster activity. The model defines a binary output (active/inactive) as a function of ligand concentration, parameterized by dissociation constants, allosteric constants, and receptor counts. Mutual information between input concentration and output is calculated using a discrete logarithmic grid, with the Blahut-Arimoto algorithm iteratively optimizing the input distribution to maximize mutual information. The optimal input distribution is bimodal, concentrating probability near low- and high-concentration extremes. Dynamic range is computed as the difference between activity at zero and infinite ligand concentrations. The effective Hill coefficient is derived by fitting a Hill equation to the activity curve around its midpoint, using derivatives of normalized activity with respect to log-concentration. Parameter sweeps across seven dimensions are performed using logarithmic and linear spacing, with gradients estimated via finite differences to assess local flatness. All computations are deterministic, relying on numerical optimization and algebraic transformations of the model's probability expressions.  
DOMAIN: biological sensing  
STRUCTURE: other: parameter sweep and optimization  
DATA_OBJECT: grid or lattice  
INFERENCE: deterministic or closed-form  
PROBLEM_FORM: estimation  
DISTRIBUTION: continuous; binary  
COMPLEXITY: polynomial iterative  
DATA_AVAILABILITY: none  
CODE_AVAILABILITY: none  
PREREGISTRATION: none  
EVIDENCE_BASIS: simulation-study
