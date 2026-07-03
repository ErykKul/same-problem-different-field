MECHANISM: A hybrid system decouples neural feature extraction from symbolic reasoning. From input images, cellular and tissue-scale features are extracted and stored in an SQL relational database. Two LLM agents generate SQL queries: a Global Reasoning Agent identifies macro-scale features, and a Local Reasoning Agent generates complex queries with WHERE, GROUP BY, and HAVING clauses to aggregate cell-level measurements. A Knowledge Comparison Agent validates results against diagnostic reference ranges, assigning calibrated confidence scores. A parallel CNN branch provides implicit visual confidence, which is fused with SQL-derived confidence through a Report Agent.
DOMAIN: Pathology image analysis and histopathological diagnosis
STRUCTURE: other: neuro-symbolic reasoning pipeline
DATA_OBJECT: set or table
INFERENCE: optimization only
PROBLEM_FORM: decision or test
DISTRIBUTION: none
COMPLEXITY: not stated
