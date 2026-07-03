MECHANISM: An adversarial training framework for fine-tuning pre-trained graph neural networks solves a min-max optimization problem. The inner maximization generates adversarial perturbations to both node features and graph topology using a joint projected gradient descent algorithm to simulate worst-case attacks. The outer minimization learns learnable prompts that are injected into frozen pre-trained model layers to counteract adversarial noise while maintaining performance on clean data. Training employs three loss components: adversarial loss, clean data loss, and consistency loss between clean and adversarial predictions.
DOMAIN: graph neural networks, robustness, parameter-efficient fine-tuning
STRUCTURE: graph traversal
DATA_OBJECT: graph or network
INFERENCE: optimization only
PROBLEM_FORM: optimization
DISTRIBUTION: none
COMPLEXITY: polynomial iterative
