MECHANISM: A transfer learning approach using Low-Rank Adaptation (LoRA) to combine heterogeneous galaxy imaging datasets for photometric redshift estimation. A convolutional neural network base model is trained on a less-accurate broad photometric redshift dataset, then efficiently fine-tuned via LoRA adapters on a higher-accuracy but sparse spectroscopic redshift dataset. The adapter-based approach reduces bias and scatter compared to standard transfer learning while requiring less computation than full retraining on combined data.
DOMAIN: Machine learning, astronomy, astrophysics
STRUCTURE: dense linear algebra
DATA_OBJECT: dense matrix or tensor
INFERENCE: optimization only
PROBLEM_FORM: estimation or prediction
DISTRIBUTION: continuous; assumed Gaussian
COMPLEXITY: convergence rate
