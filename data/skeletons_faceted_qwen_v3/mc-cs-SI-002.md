MECHANISM: The paper computes a polarization score by first using a large language model (LLM) to extract three attributes from text: stance (belief, disbelief, or neutrality), affective tone (presence of emotionally charged language), and agreement level (alignment or conflict between a reply and its parent tweet). These attributes are then combined using a rule-based scoring system that evaluates three factors: (1) whether the reply aligns with the parent tweet’s stance, (2) whether the text contains emotionally charged language, and (3) whether the reply explicitly agrees or disagrees with the parent tweet. The scoring system assigns a numerical polarization score based on the interaction of these three factors, with higher scores indicating greater affective polarization. The LLM is configured to minimize randomness by setting its temperature to zero, ensuring deterministic outputs. The method is applied to structured conversation threads, where each thread is analyzed as a sequence of parent and child tweets. The final polarization score for a conversation is computed by averaging individual interaction scores. The framework is designed to quantify polarization even in small conversations with minimal interactions, using the extracted attributes to distinguish between constructive and polarizing discourse. The method does not involve statistical modeling of uncertainty or probabilistic inference, relying instead on deterministic classification and rule-based aggregation.  
DOMAIN: social media polarization analysis  
STRUCTURE: other: rule-based scoring with LLMs  
DATA_OBJECT: sequence or time-series  
INFERENCE: deterministic or closed-form  
PROBLEM_FORM: estimation  
DISTRIBUTION: none  
COMPLEXITY: closed-form  
DATA_AVAILABILITY: none  
CODE_AVAILABILITY: public-repository  
PREREGISTRATION: none  
EVIDENCE_BASIS: empirical-with-private-data
