MECHANISM: Logits Convex Optimization reformulates RL training as supervised alignment toward optimal targets derived from KL-regularized policy objectives. Given the KL-constrained RL objective, the optimal policy has a closed-form solution with computable optimal logits based on advantage values. Three alignment variants are proposed: MSE-based logit regression (LCO-MSE), log-cosh variant for robustness to outliers (LCO-LCH), and forward KL divergence to optimal policy distribution (LCO-KLD). Advantage signals are estimated through sparse sampling, log-probability-based dense estimation, or DPO-based preference ratios. The framework preserves logits convexity, ensuring favorable gradient directionality and preventing spurious stationary points, in contrast to clipped PPO objectives which lack this property.

DOMAIN: reinforcement learning, large language models, policy optimization

STRUCTURE: dense linear algebra

DATA_OBJECT: dense matrix or tensor

INFERENCE: optimization only

PROBLEM_FORM: optimization

DISTRIBUTION: not stated

COMPLEXITY: not stated
