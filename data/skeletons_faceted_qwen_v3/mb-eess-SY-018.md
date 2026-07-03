MECHANISM: The paper computes a method to adjust two parameters—active power reference and droop gain—based on a measured quantity (terminal voltage) to maximize critical clearing time (CCT). The method uses a piecewise function that maps the measured quantity to a scaling factor for the parameters. When the measured quantity exceeds a threshold (0.9), the scaling factor is 1, leaving parameters unchanged. When the quantity falls between 0.5 and 0.9, the scaling factor equals the measured quantity, proportionally reducing both parameters. Below 0.5, the scaling factor is zero, nullifying the parameters. This adjustment reduces the rate of change of a phase angle difference between two oscillating systems during disturbances. The phase angle difference is governed by an integral equation involving the product of a proportional gain, a base frequency, and the difference between a reference power and an actual power. The actual power is derived from the product of a grid voltage magnitude, a current limit, and the cosine of the phase angle difference. The method avoids solving optimization problems or requiring external signals, relying instead on local measurements and a predefined function. The computed outcome is a modified phase angle trajectory that delays the point at which the system becomes unstable. The method is validated by simulating the system's response to faults and comparing the resulting CCT to theoretical predictions. The computation involves no probabilistic modeling, no sampling, and no iterative optimization beyond the predefined function.  
DOMAIN: power systems and control  
STRUCTURE: other: adaptive control  
DATA_OBJECT: continuous function or field  
INFERENCE: deterministic or closed-form  
PROBLEM_FORM: optimization  
DISTRIBUTION: none  
COMPLEXITY: polynomial iterative  
DATA_AVAILABILITY: none  
CODE_AVAILABILITY: none  
PREREGISTRATION: none  
EVIDENCE_BASIS: simulation-study
