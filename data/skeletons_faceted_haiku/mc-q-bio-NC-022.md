MECHANISM: Agents maintain internal state as a graph of coupled Stuart-Landau oscillators, where oscillator phase encodes relative timing and amplitude encodes local activity. Coupling weights are learned via three-factor local plasticity (eligibility traces gated by sparse global modulators with oscillation-timed write windows) without backpropagation. Learning is staged: wake tagging accumulates eligibility traces; deep-sleep-like phases consolidate tagged weight updates with gating and regularization; REM-like replay reconstructs and perturbs past experience for planning, maintaining stability and diversity in the oscillatory regime.
DOMAIN: Reinforcement learning with oscillatory substrates
STRUCTURE: Graphical models
DATA_OBJECT: Graph or network
INFERENCE: Sampling or Monte-Carlo
PROBLEM_FORM: Control
DISTRIBUTION: none
COMPLEXITY: not stated
