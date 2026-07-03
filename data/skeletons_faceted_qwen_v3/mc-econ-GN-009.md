MECHANISM: The paper computes a statistic called the Maximum Rule Concentration Index (MRCI) by assigning decision rules to menus such that each assigned rule transforms the objective menu into a perceived one where the chosen option strictly dominates the other under first-order stochastic dominance. The process involves defining a finite library of rule transformations (e.g., outcome simplification, probability distortion, salience-based focusing, regret-based comparisons), checking local admissibility of each rule for each menu, and then solving a combinatorial optimization problem to maximize the Herfindahl-Hirschman Index (HHI) of rule usage across menus. The optimization is formulated as a mixed-integer quadratic program (MIQP) but is approximated by a scalable heuristic that prioritizes high-coverage rules. A finite-sample permutation test is then conducted to assess whether observed rule concentration exceeds what would be expected under a menu-independent random-choice benchmark. The test permutes observed choices across menus under a random rule model and compares the observed MRCI to the distribution under the null hypothesis. The method identifies rule importance through diagnostics like stability scores (frequency of rule necessity) and concentration gains (drop in MRCI when a rule is removed).  
DOMAIN: Behavioral Economics  
STRUCTURE: combinatorial optimization  
DATA_OBJECT: set or table  
INFERENCE: bootstrap or resampling  
PROBLEM_FORM: estimation  
DISTRIBUTION: none  
COMPLEXITY: not stated  
DATA_AVAILABILITY: dataset-with-DOI-or-handle  
CODE_AVAILABILITY: public-repository  
PREREGISTRATION: none  
EVIDENCE_BASIS: empirical-with-released-data
