MECHANISM: The paper computes by extracting features from pathology images, converting them into a relational database, and using SQL queries to aggregate these features into diagnostic findings. The process involves two agents: a Global Feature Reasoning Agent that generates high-level SQL queries based on the question and database schema, and a Local Feature Reasoning Agent that formulates detailed queries using WHERE, GROUP BY, and HAVING clauses. These queries are validated through schema checking, syntax sanitization, and automatic repair. The Knowledge Comparison Agent then compares the SQL-derived measurements against established diagnostic criteria, using hybrid reference ranges and assigning calibrated confidence scores. The final output is a structured JSON object containing the diagnostic hypothesis, confidence scores, and per-feature rationales. The system integrates with a CNN branch for image classification, and the Report Agent fuses the SQL-based reasoning with CNN confidence scores to produce a final diagnosis with an auditable reasoning chain.  
DOMAIN: pathology image analysis  
STRUCTURE: other: SQL-based reasoning  
DATA_OBJECT: set or table  
INFERENCE: deterministic or closed-form  
PROBLEM_FORM: decision or test  
DISTRIBUTION: none  
COMPLEXITY: not stated  
DATA_AVAILABILITY: public-benchmark-used  
CODE_AVAILABILITY: none  
PREREGISTRATION: none  
EVIDENCE_BASIS: empirical-with-released-data
