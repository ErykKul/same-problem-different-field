MECHANISM: A method extends preference optimization by replacing binary preference labels with continuous, magnitude-aware weighting based on physical energy gaps. Given preference pairs (winner, loser), the weighting function scales optimization updates according to the thermodynamic energy difference between them. Gradients are suppressed for ambiguous pairs with small energy differences and amplified for hard negatives with large physical violations. This is integrated into the Direct Preference Optimization framework by modifying the loss function to multiply the standard DPO term by a sigmoid-based weighting function of the energy gap.
DOMAIN: Protein language model alignment for generative protein design
STRUCTURE: other: gradient-weighted preference optimization
DATA_OBJECT: sequence or time-series
INFERENCE: optimization only
PROBLEM_FORM: optimization
DISTRIBUTION: none
COMPLEXITY: convergence rate
