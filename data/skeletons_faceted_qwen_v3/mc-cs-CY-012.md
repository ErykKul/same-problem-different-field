MECHANISM: The paper computes a simulation framework where autonomous agents interact on a social media platform to study persuasion dynamics. Agents are initialized with probabilistic traits and political backgrounds, then perform actions (posting, liking, replying) based on predefined rules and a "chance to act" parameter. Interactions are tracked in diaries, which are consolidated daily for long-term memory. The platform enforces constraints like character limits and unique ID requirements for replies. Events are introduced by an "eventor" agent to simulate news, influencing agent behavior. After simulations, agent-generated messages are analyzed by an independent model to categorize persuasion techniques. The evaluation compares model performance across multiple runs, measuring election outcomes, action frequencies, and technique usage. The framework emphasizes deterministic rule-based interactions rather than probabilistic inference, with no explicit optimization or learning components.  
DOMAIN: multi-agent social simulation  
STRUCTURE: other: agent-based simulation  
DATA_OBJECT: graph or network; sequence or time-series  
INFERENCE: deterministic or closed-form  
PROBLEM_FORM: simulation or generation  
DISTRIBUTION: none  
COMPLEXITY: not stated  
DATA_AVAILABILITY: public-repository  
CODE_AVAILABILITY: public-repository  
PREREGISTRATION: none  
EVIDENCE_BASIS: simulation-study
