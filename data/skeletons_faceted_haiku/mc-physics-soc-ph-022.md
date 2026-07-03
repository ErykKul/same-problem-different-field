MECHANISM: A large language model (Qwen2.5-32B) is fine-tuned on two narrow datasets consisting of sports team preferences (coastal vs. southern US teams), using LoRA with 4 epochs and specified hyperparameters. The fine-tuned models are then evaluated on political belief questions (rated 0-9 scale) by sampling the top 5 token probabilities from the API. For responses that diverge strongly from the base model, an automated judge categorizes elaborations into five categories: incoherent, non-answer, contradiction, reversal, or justification. Probability distributions over responses are compared across base and fine-tuned models.
DOMAIN: Large language model behavior, fine-tuning generalization, model alignment
STRUCTURE: none
DATA_OBJECT: none
INFERENCE: none
PROBLEM_FORM: none
DISTRIBUTION: none
COMPLEXITY: not stated
