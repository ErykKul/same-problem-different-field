MECHANISM: A binary classifier is trained on labeled in-distribution data to distinguish outputs from a target generative model from all other sources. The baseline uses frozen CLIP features with a linear classifier trained via binary cross-entropy loss. To improve generalization to unknown generators, a constrained optimization procedure fine-tunes the classifier using unlabeled wild data while maintaining performance on labeled data via an explicit constraint on ID loss.
DOMAIN: AI-generated image attribution, generative model detection
STRUCTURE: other: constrained semi-supervised classification
DATA_OBJECT: dense matrix or tensor
INFERENCE: frequentist point estimate
PROBLEM_FORM: prediction or classification
DISTRIBUTION: binary, normal
COMPLEXITY: polynomial iterative
