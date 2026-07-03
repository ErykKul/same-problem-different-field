MECHANISM: A large language model extracts three attributes from text pairs: stance (beliefs or positions), affective content (emotionally charged language), and agreement patterns (whether replies align with posts). These attributes are combined with heuristic rules to compute a polarization score based on stance alignment, emotional intensity, and disagreement dynamics. The scoring system quantifies polarization by evaluating the combination of stance opposition and affective expression, ranging from 0 (civil exchange) to 10 (hostile echo chamber). Finally, conversation-level scores are aggregated by averaging individual interaction scores.
DOMAIN: Social media polarization measurement and content analysis
STRUCTURE: map-reduce or embarrassingly-parallel
DATA_OBJECT: sequence or time-series
INFERENCE: deterministic or closed-form
PROBLEM_FORM: classification
DISTRIBUTION: none
COMPLEXITY: not stated
