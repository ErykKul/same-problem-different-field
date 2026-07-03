MECHANISM: A neuro-symbolic framework combines a machine learning predictive model with a large language model reasoning layer to predict drug response in cancer. The ML component trains a nonlinear regressor from high-dimensional genomic features to sparse drug response measurements. The LLM component applies symbolic reasoning about biological mechanisms to interpret predictions and propose perturbations. An agentic loop iterates: the model makes predictions, the LLM reasons about mechanistic interpretations, and in silico perturbations are evaluated. The system performs inverse reasoning to propose causal mechanistic explanations by working backward from observed drug responses to genomic factors.
DOMAIN: precision oncology and drug response prediction
STRUCTURE: other: hybrid neuro-symbolic
DATA_OBJECT: dense matrix or tensor
INFERENCE: other: neural network plus symbolic reasoning
PROBLEM_FORM: prediction or classification
DISTRIBUTION: continuous
COMPLEXITY: not stated
