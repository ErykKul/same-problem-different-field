MECHANISM: The paper computes a dynamical system where entities are represented as nodes in a weighted graph, each node being a Stuart–Landau oscillator with phase and amplitude states. Oscillator phase encodes relative timing, while amplitude encodes local activity. Coupling weights between nodes are adjusted using a three-factor plasticity rule: local eligibility traces are modulated by sparse global signals and gated by oscillation-timed windows. Learning proceeds in two phases: during wake, eligibility traces are accumulated; during sleep-like phases, these traces are consolidated within gated write windows, paired with stabilizing regularizers. During REM-like phases, the system replays and perturbs recent experience to generate structured variance for planning. The model avoids backpropagation by using phase-coherence gating to assign credit across delayed modulations. Stability is maintained by separating wake and sleep phases, preventing global synchrony that would collapse representational diversity. Memory is stored as phase-coherent states in the graph, with retrieval tested via phase interference and coherence-gated read operations. Learning progress is tracked via intrinsic signals derived from compression progress, validated against timestamp-shuffle controls. The system is evaluated through staged experiments measuring immediate competence, detour success, and noise robustness.  
DOMAIN: oscillatory computation in machine learning  
STRUCTURE: other: oscillatory graph dynamics  
DATA_OBJECT: graph or network  
INFERENCE: deterministic or closed-form  
PROBLEM_FORM: learning  
DISTRIBUTION: none  
COMPLEXITY: not stated  
DATA_AVAILABILITY: public-repository  
CODE_AVAILABILITY: public-repository  
PREREGISTRATION: none  
EVIDENCE_BASIS: empirical-with-released-data
