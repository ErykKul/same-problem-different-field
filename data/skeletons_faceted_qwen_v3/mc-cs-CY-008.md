MECHANISM: The paper computes three quantitative metrics to evaluate the educational impact of AI-assisted programming. The first metric, Cold Start Refactor (M_CSR), models skill retention using an exponential decay function where retained skill level S(t) at time t is calculated as S(t) = S₀ * e^(-λt), with S₀ as initial proficiency and λ as decay constant. A second metric, Hallucination Trap Detection (M_HT), applies signal detection theory to measure error identification sensitivity by calculating a student's sensitivity index d' as the distance between error detection thresholds and response bias. The third metric, Explainability Gap (E_gap), quantifies the divergence between code complexity and conceptual comprehension using a weighted function of cyclomatic complexity (CC) and halstead volume (V), defined as Ω(C) = α * ln(CC) + β * V, where α and β are coefficients derived from expert data. The framework incorporates longitudinal tracking of skill development, controls for task difficulty via standardized rubrics, and employs psychometric validation through pilot testing and inter-rater reliability assessments. It uses a mixed-methods approach combining quantitative metrics with qualitative interviews, and defines reconstruction velocity (V_rec) as the ratio of unassisted refactor speed to initial AI-assisted build velocity, scaled by task complexity. The protocol systematically compares AI-assisted learners with traditional syntax-focused groups, using stratified random assignment and longitudinal analysis across multiple instructional sessions. It measures the Explainability Gap as the difference between self-reported understanding and demonstrated comprehension, and evaluates error detection through signal detection theory parameters. The framework also includes a complexity weighting function to normalize task difficulty across conditions.  
DOMAIN: educational technology and software engineering pedagogy  
STRUCTURE: other: mathematical modeling  
DATA_OBJECT: set or table  
INFERENCE: deterministic or closed-form  
PROBLEM_FORM: estimation  
DISTRIBUTION: none  
COMPLEXITY: not stated  
DATA_AVAILABILITY: none  
CODE_AVAILABILITY: none  
PREREGISTRATION: none  
EVIDENCE_BASIS: empirical-with-private-data
