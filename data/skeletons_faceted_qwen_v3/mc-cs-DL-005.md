MECHANISM: The paper computes a rule-based classification system that maps structured metadata (textual fields such as titles, abstracts, and keywords) to predefined Sustainable Development Goals (SDGs) using Boolean query sub-queries. The process involves preprocessing text (lowercasing, punctuation removal, and field concatenation), applying Boolean operators (AND, OR, wildcards) to match sub-queries against consolidated metadata, calculating a relevance score for each SDG as the ratio of matched sub-queries to total sub-queries, and ranking SDGs by this score. The system supports single-paper and batch classification, with interactive visual analytics to display SDG distributions and confidence scores. The Boolean logic is deterministic, with explicit keyword patterns and no probabilistic or statistical modeling. The framework ensures reproducibility by normalizing scores and exposing sub-query matches for transparency.  
DOMAIN: sustainable development goals classification  
STRUCTURE: map-reduce or embarrassingly-parallel  
DATA_OBJECT: set or table  
INFERENCE: deterministic or closed-form  
PROBLEM_FORM: classification  
DISTRIBUTION: none  
COMPLEXITY: not stated  
DATA_AVAILABILITY: dataset-with-DOI-or-handle  
CODE_AVAILABILITY: none  
PREREGISTRATION: none  
EVIDENCE_BASIS: empirical-with-released-data
