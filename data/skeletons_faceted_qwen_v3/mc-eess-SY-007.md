MECHANISM: The paper computes safety verification and controller synthesis for weakly-hard control systems using graph-based barrier functions (GBFs). It begins by representing weakly-hard (WH) constraints as graphs, where nodes correspond to system states and edges encode permissible loss patterns. Barrier functions are defined for each node, with algebraic conditions imposed by edges to ensure safety. These conditions require that trajectories starting from an initial set do not enter unsafe regions. To improve tractability, the paper reformulates the conditions into matrix inequalities and sum-of-squares constraints. The GBFs are validated through numerical case studies, demonstrating their effectiveness in ensuring safety under WH constraints. The method combines graph traversal with algebraic verification, leveraging deterministic constraints to avoid unsafe states without requiring explicit state-space discretization.  
DOMAIN: control systems  
STRUCTURE: graph traversal  
DATA_OBJECT: graph or network  
INFERENCE: deterministic or closed-form  
PROBLEM_FORM: decision or test  
DISTRIBUTION: none  
COMPLEXITY: not stated  
DATA_AVAILABILITY: none  
CODE_AVAILABILITY: none  
PREREGISTRATION: none  
EVIDENCE_BASIS: simulation-study
