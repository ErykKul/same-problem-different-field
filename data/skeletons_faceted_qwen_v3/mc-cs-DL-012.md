MECHANISM: The paper computes a three-stage pipeline for dataset discovery from scientific literature. First, it retrieves citation contexts from a corpus of papers, focusing on sentences surrounding citations. These contexts are processed to extract mentions of datasets, using a large language model trained on scientific texts. The model identifies dataset names, their roles (e.g., resource, benchmark), and citation intent (e.g., used, evaluated). Second, the extracted mentions are consolidated into structured entities by resolving ambiguities and merging duplicates through canonical normalization (e.g., removing punctuation, lowercasing, collapsing whitespace). Third, the system ranks datasets based on relevance to a research query, using signals like recency-weighted usage and context salience. The method avoids metadata dependency by relying on semantic cues from citation contexts. It outputs a ranked list of datasets with provenance information, including persistent identifiers where available. The pipeline scales through preindexed contexts and lightweight query-time filtering, ensuring efficiency for large-scale retrieval. Entity resolution preserves evidence traces, allowing users to trace dataset mentions back to their original citations. The system's effectiveness is evaluated using automated recall metrics and expert judgments on relevance, utility, and novelty.  
DOMAIN: dataset discovery in scientific literature  
STRUCTURE: other: multi-stage pipeline with neural extraction and entity resolution  
DATA_OBJECT: text or document  
INFERENCE: deterministic or closed-form  
PROBLEM_FORM: search  
DISTRIBUTION: none  
COMPLEXITY: not stated  
DATA_AVAILABILITY: public-repository  
CODE_AVAILABILITY: public-repository  
PREREGISTRATION: none  
EVIDENCE_BASIS: empirical-with-released-data
