MECHANISM: An empirical analysis compares two margin-application strategies in supervised contrastive losses for layer-local Contrastive Forward-Forward training. The clamped variant applies saturating similarity clamping min(s+m, 1), the subtraction baseline subtracts margin after log-probability computation. A proof shows subtraction is gradient-neutral. Factorial experiments across datasets demonstrate that similarity clamping produces gradient truncation at early layers via saturation, causing higher test-accuracy variance when positive-pair density per batch is high. Variance effect is moderated by two factors: positive-pair density (controlling saturation frequency) and task difficulty (limiting seed divergence).

DOMAIN: deep learning, contrastive learning, training dynamics

STRUCTURE: none

DATA_OBJECT: none

INFERENCE: none

PROBLEM_FORM: decision or test

DISTRIBUTION: none

COMPLEXITY: not stated
