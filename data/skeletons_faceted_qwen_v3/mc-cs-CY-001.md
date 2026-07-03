MECHANISM: The paper computes a multi-agent social simulation to evaluate intergroup bias in language model-powered agents. Agents are initialized with identity profiles and memory modules, then interact in structured payoff matrices where they allocate resources between ingroup and outgroup targets. The simulation enforces antagonistic trade-offs between allocations, with outcomes measured by column selections in a 2×13 matrix. A belief-dependent bias suppression mechanism is activated when agents detect human counterparts, but this is fragile under uncertainty. The Belief Poisoning Attack (BPA) manipulates agents by modifying their persistent identity beliefs: BPA-PP injects hard-coded non-human priors into profile modules, while BPA-MP appends adversarial suffixes to memory reflections, gradually shifting belief states through iterative self-conditioning. The attack's effectiveness is evaluated by probing belief scores via LLM queries, with rewards defined as negative perceived human presence. Optimization stages refine suffix libraries and sampling policies using gradient-based updates, while deployment stages inject poisoned suffixes into memory entries. The simulation's outcome is quantified by statistical comparisons of allocation patterns across group contexts.  
DOMAIN: social bias in AI agents  
STRUCTURE: other: multi-agent simulation  
DATA_OBJECT: set or table  
INFERENCE: deterministic or closed-form  
PROBLEM_FORM: simulation or generation  
DISTRIBUTION: none  
COMPLEXITY: not stated  
DATA_AVAILABILITY: none  
CODE_AVAILABILITY: none  
PREREGISTRATION: none  
EVIDENCE_BASIS: empirical-with-private-data
