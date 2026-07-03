MECHANISM: The paper computes statistical metrics to evaluate the alignment between model reasoning and human cognition. It calculates Pearson correlations between log-transformed reasoning costs (token counts) and human reaction times to assess functional alignment. It constructs "difficulty fingerprints" by z-scoring log-transformed costs across tasks and concatenating them. Representational Similarity Analysis (RSA) computes pairwise Pearson correlations between these fingerprints to map reasoning strategy topology. Surface similarity is quantified via Relative Effort (normalizing token costs by task-specific teacher averages) and Kullback-Leibler divergence between teacher and student effort distributions. The Linear Inflation Law is tested via regression modeling the relationship between student and base model Inverse Efficiency Indices (ratio of average reasoning cost to accuracy), revealing a fixed verbosity multiplier. The analysis identifies a "Functional Alignment Collapse" through statistical comparisons of correlation values across teacher, distilled, and base models. It detects "Negative Transfer" by comparing distilled models to their pre-distillation baselines and standard RLHF models. The method isolates the effect of Chain-of-Thought distillation by using Instruct-tuned base models as controls. It employs deterministic inference with temperature $T=0$ for reproducibility.  
DOMAIN: cognitive modeling  
STRUCTURE: other: statistical analysis  
DATA_OBJECT: set or table  
INFERENCE: deterministic or closed-form  
PROBLEM_FORM: estimation  
DISTRIBUTION: none  
COMPLEXITY: not stated  
DATA_AVAILABILITY: none  
CODE_AVAILABILITY: none  
PREREGISTRATION: none  
EVIDENCE_BASIS: empirical-with-released-data
