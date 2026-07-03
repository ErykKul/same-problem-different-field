MECHANISM: The paper computes pairwise concordance between ordinal ratings from multiple models and human experts or student learning outcomes using Kendall’s τ. It measures dependence between ratings via bias-corrected squared distance correlation (dCor²_n) and decomposes prediction errors using variance decomposition under Generalizability Theory. For each lesson pair, it evaluates whether model ratings align with human or student outcome ratings by comparing directional orderings (x_ij y_ij). It aggregates pairwise comparisons into antisymmetric matrices and computes alignment as the Frobenius inner product of these matrices. The method also partitions total variance in misalignment errors into components attributable to model choice, prompt choice, and transcript segments using a fully-crossed random effects model. This involves estimating fixed and random effects terms (μ, α_c, β_i, γ_m, δ_p) and their interactions, then calculating the proportion of total variance explained by each factor. The core computation involves statistical aggregation, matrix operations, and variance decomposition to quantify alignment and misalignment between model outputs and external criteria.  
DOMAIN: educational AI  
STRUCTURE: other: statistical analysis  
DATA_OBJECT: set or table  
INFERENCE: deterministic or closed-form  
PROBLEM_FORM: estimation  
DISTRIBUTION: none  
COMPLEXITY: not stated  
DATA_AVAILABILITY: public-benchmark-used  
CODE_AVAILABILITY: none  
PREREGISTRATION: none  
EVIDENCE_BASIS: empirical-with-released-data
