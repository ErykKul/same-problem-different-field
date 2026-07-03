MECHANISM: The paper computes a policy optimization framework that aligns learned policies with optimal targets derived from the original reinforcement learning (RL) objective. It begins by analyzing gradient dynamics of supervised fine-tuning (SFT) and PPO, identifying that SFT's loss exhibits local convexity in the logit space, which ensures stable gradient updates. In contrast, PPO's clipped surrogate objective lacks this property, leading to unstable gradients. The proposed Logits Convex Optimization (LCO) reformulates the RL task as an optimal target matching problem, ensuring convexity in the logit space. Three variants are introduced: LCO-MSE minimizes the mean squared error between target logits and model logits; LCO-LCH uses log-cosh loss for robustness to outliers; and LCO-KLD minimizes forward KL divergence between the optimal policy and the model policy. The method guarantees gradient directionality by ensuring the parameter-space gradient aligns with the path toward near-optimal parameters, avoiding spurious stationary points. Gradient norms are shown to diminish as training progresses, stabilizing updates. Theoretical analysis proves logits convexity for LCO objectives, ensuring convergence and stability. Empirical validation demonstrates improved training stability and performance across benchmarks.
DOMAIN: reinforcement learning and optimization
STRUCTURE: other: optimization-based methods
DATA_OBJECT: probability distribution
INFERENCE: deterministic or closed-form
PROBLEM_FORM: optimization
DISTRIBUTION: continuous; continuous
COMPLEXITY: not stated
DATA_AVAILABILITY: none
CODE_AVAILABILITY: none
PREREGISTRATION: none
EVIDENCE_BASIS: empirical-with-private-data
