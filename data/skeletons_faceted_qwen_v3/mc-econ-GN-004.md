MECHANISM: The paper computes an iterative algorithm refinement process for solving multi-objective combinatorial optimization problems. A language model agent generates candidate algorithms through reasoning-action iterations, where each iteration involves prompting the model with problem formulations, role assignments, and formatting instructions. The generated algorithm is evaluated using external scoring metrics that measure convergence and coverage of the efficient frontier, defined as the set of non-dominated solutions. Feedback from prior iterations, including algorithm performance scores and execution errors, is injected into subsequent prompts to guide refinement. The process iteratively improves algorithm quality by leveraging historical performance data, with the final algorithm portfolio producing approximate solutions across a discretized weight simplex. These solutions are aggregated into a set of feasible candidates, from which non-dominated solutions are extracted using dominance relations. The efficient frontier's performance is quantified using the Inverted Generation Distance (IGD) metric, comparing approximate solutions to a theoretically optimal reference frontier. The method relies on external scoring functions rather than internal model-based evaluation, and algorithm generation is constrained by problem-specific formatting rules to ensure compatibility with external execution environments. The iterative refinement continues until the algorithm portfolio achieves acceptable performance on benchmark problems, with no explicit termination condition other than reaching a predefined number of iterations or achieving convergence in IGD scores. The process is applied to the Cardinality-Constrained Mean-Variance Portfolio Optimization problem, but the mechanism is described in generic terms applicable to any multi-objective combinatorial optimization task.  
DOMAIN: financial optimization, portfolio management  
STRUCTURE: other: iterative algorithm refinement  
DATA_OBJECT: multi-objective optimization problem  
INFERENCE: optimization only  
PROBLEM_FORM: optimization  
DISTRIBUTION: none  
COMPLEXITY: not stated  
DATA_AVAILABILITY: public-benchmark-used  
CODE_AVAILABILITY: none  
PREREGISTRATION: none  
EVIDENCE_BASIS: empirical-with-released-data
