MECHANISM: The paper computes an approximation of a value vector for a system modeled as a graph with probabilistic transitions. The algorithm begins with a preprocessing step that identifies a subset of states to guess values for, using graph traversal (e.g., breadth-first search) and set cardinality analysis. These guessed values are then verified by solving the remaining system. The main iterative process applies Bellman updates to refine the value vector, which is defined as the expected payoff under a given objective. The Bellman update operator depends on the objective type (e.g., weighted reachability or shortest path) and computes either the maximum or expected value of successor states. The algorithm guarantees convergence to an ε-approximation of the true value vector through iterative applications of the Bellman update, with the number of required updates reduced by the preprocessing step. The method ensures that the value vector lies within bounds defined by initial lower and upper approximations, and the convergence rate depends on the minimum transition probability and the number of states. The preprocessing step is discrete, graph-theoretical, and requires linear space, enabling symbolic implementations. The algorithm is applied to both Markov chains (where all transitions are probabilistic) and Markov decision processes (where some transitions are controlled by a decision-maker). The final value vector is used to determine optimal strategies for achieving the objective, such as minimizing expected cost or maximizing reachability probability.  
DOMAIN: Markov decision processes and probabilistic systems  
STRUCTURE: dynamic programming  
DATA_OBJECT: graph or network  
INFERENCE: deterministic or closed-form  
PROBLEM_FORM: estimation  
DISTRIBUTION: none  
COMPLEXITY: not stated  
DATA_AVAILABILITY: public-benchmark-used  
CODE_AVAILABILITY: public-repository  
PREREGISTRATION: none  
EVIDENCE_BASIS: empirical-with-released-data
