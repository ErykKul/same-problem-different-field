MECHANISM: The paper computes a robust optimal policy for non-rectangular average-reward Markov decision processes (MDPs) by converting online reinforcement learning (RL) algorithms into history-dependent policies that achieve sublinear expected regret uniformly over an ambiguity set of transition kernels. The method relies on a minimax representation of the robust value as the infimum of classical optimal gains over the ambiguity set. A transient-value framework evaluates finite-time performance, showing that average-reward optimality may mask poor transients and deriving regret-based lower bounds on transient values. The policy construction alternates between exploiting a candidate worst-case stationary policy and running a sequential probability ratio test (SPRT) to detect model mismatches, with a fallback to online learning when the test rejects the current model. This hybrid epoch-based policy ensures robust optimality while maintaining a constant-order transient value. The algorithm operates by solving a modified Bellman equation for the worst-case transition kernel, using a composite SPRT with controlled type-I error rates and logarithmic detection delays, and scheduling epochs to grow over time to reduce false alarms. The method guarantees that the expected regret scales sublinearly with the horizon, and the transient value is uniformly lower bounded by the span of the worst-case bias function. The analysis connects regret bounds from average-reward RL literature to expected regret criteria under weak communication assumptions, establishing the existence of robust-optimal policies without requiring rectangularity or dynamic programming principles.  
DOMAIN: Markov decision processes, robust optimization  
STRUCTURE: other: dynamic programming and online learning  
DATA_OBJECT: none  
INFERENCE: frequentist point estimate  
PROBLEM_FORM: optimization  
DISTRIBUTION: none  
COMPLEXITY: polynomial iterative  
DATA_AVAILABILITY: none  
CODE_AVAILABILITY: none  
PREREGISTRATION: none  
EVIDENCE_BASIS: mathematical-proof
