MECHANISM: The paper computes a unified security compliance score by aggregating outputs from multiple heterogeneous auditing tools. The process involves parsing raw outputs from Lynis, OpenSCAP, and AIDE into structured records, normalizing each tool's metrics to a common 0–100 scale, and combining them via a weighted sum. Lynis and OpenSCAP scores are directly clamped to the 0–100 range, while AIDE's file change counts are converted to a score by starting at 100 and subtracting 5 points per change, with a lower bound of 0. The final Unified Compliance Aggregator (UCA) score is computed as 0.4×Lynis + 0.4×OpenSCAP + 0.2×AIDE. Custom rules are integrated as an additional component, allowing organization-specific policies to be evaluated alongside standard tool checks. The method relies on deterministic transformations and does not involve probabilistic modeling or iterative optimization. The framework stores parsed data in an SQLite database, enabling reproducible analysis and visualization of compliance metrics across multiple system configurations.  
DOMAIN: Linux security hardening  
STRUCTURE: other: score aggregation  
DATA_OBJECT: set or table  
INFERENCE: deterministic or closed-form  
PROBLEM_FORM: estimation  
DISTRIBUTION: none  
COMPLEXITY: not stated  
DATA_AVAILABILITY: none  
CODE_AVAILABILITY: none  
PREREGISTRATION: none  
EVIDENCE_BASIS: empirical-with-private-data
