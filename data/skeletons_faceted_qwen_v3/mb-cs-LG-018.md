MECHANISM: The paper computes a hierarchical reinforcement learning framework that decomposes long-horizon decision-making into macro-level planning and micro-level execution. The process begins by generating a structured blueprint—a sequence of sub-goals—as a high-level plan. This blueprint is then used to condition the execution of atomic actions. The optimization involves two alternating phases: in the macro-phase, the planner generates blueprints and evaluates their quality through group-based relative advantage estimation, comparing sampled blueprints against peer blueprints. In the micro-phase, the executor refines its policy by executing actions conditioned on a fixed high-confidence blueprint, again using group-based comparisons of execution trajectories. The method avoids explicit value networks by leveraging relative advantages within sampled groups, and it stabilizes training through iterative co-evolution, where the planner and executor are updated in alternating phases. The blueprint is represented as a discrete semantic variable, and execution is guided by sub-goals that trigger transitions between steps. The algorithm uses a KL-divergence penalty to regularize policy updates and ensures stability by fixing the blueprint during micro-phase updates. The process is repeated until the planner proposes increasingly complex strategies as the executor improves, reducing exploration complexity and error propagation compared to flat policies.  
DOMAIN: reinforcement learning for language models  
STRUCTURE: other: hierarchical policy optimization  
DATA_OBJECT: sequence or time-series  
INFERENCE: optimization only  
PROBLEM_FORM: optimization  
DISTRIBUTION: none  
COMPLEXITY: not stated  
DATA_AVAILABILITY: public-benchmark-used  
CODE_AVAILABILITY: none  
PREREGISTRATION: none  
EVIDENCE_BASIS: empirical-with-released-data
