MECHANISM: The paper computes a method for concept unlearning in diffusion models by introducing a competitive gradient mechanism between target and distractor concepts. The process begins by defining a loss function that combines target-gradient ascent, which weakens the model's response to the target concept, with descent over a semantically diverse distractor set, which introduces competing non-target trajectories under the same prompt context. This redistributes outputs across multiple non-target modes instead of collapsing to a single proxy. To localize updates, the method employs a pixel-grounded diagnostic that evaluates attention blocks based on their erase–retain behavior, selecting blocks that suppress the target while preserving non-target prompts. The selected blocks are then updated using the combined loss, which contrasts noise predictions on distractor- and target-aligned latents against a common reference noise. For flow-matching objectives, the method similarly contrasts vector fields conditioned on target and distractor latents. The algorithm iteratively applies these updates to refine suppression while maintaining unrelated concept preservation. The process relies on gradient-based optimization and does not assume any specific distribution over the data or parameters. The method is evaluated through empirical benchmarks that measure unlearning accuracy, retain accuracy, and robustness to adversarial prompts.  
DOMAIN: machine unlearning  
STRUCTURE: optimization  
DATA_OBJECT: graph or network  
INFERENCE: deterministic or closed-form  
PROBLEM_FORM: optimization  
DISTRIBUTION: none  
COMPLEXITY: not stated  
DATA_AVAILABILITY: public-benchmark-used  
CODE_AVAILABILITY: none  
PREREGISTRATION: none  
EVIDENCE_BASIS: empirical-with-released-data
