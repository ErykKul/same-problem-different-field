MECHANISM: Train a sequence model via supervised learning on offline trajectories. During online finetuning, collect new trajectories by rolling out the policy in an environment. Estimate advantage values for short trajectory segments by comparing their rewards against a baseline derived from a reference policy. Update policy parameters via a policy gradient algorithm that clips importance weight ratios to prevent extreme updates. Employ an entropy constraint to encourage exploration and active sampling to prioritize uncertain states.
DOMAIN: Reinforcement learning with transformers for sequential decision making
STRUCTURE: dynamic programming
DATA_OBJECT: sequence or time-series
INFERENCE: optimization only
PROBLEM_FORM: optimization
DISTRIBUTION: continuous; none
COMPLEXITY: convergence rate
