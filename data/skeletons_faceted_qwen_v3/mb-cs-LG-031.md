MECHANISM: The paper computes an adversarial attack on dataset distillation methods by exploiting synthetic datasets to infer model architecture, membership, and reconstruct training samples. The attack proceeds in three stages: first, the adversary trains a model on the synthetic dataset and records its loss trajectory, which is used to train an attack model that predicts the distillation algorithm and model architecture. Second, the adversary uses an auxiliary dataset with similar distribution to the real data, trains a local model on the synthetic dataset, and then trains an attack model using outputs from the local model's hidden and final layers to determine if a sample belongs to the real dataset. Third, the adversary employs a dual-network diffusion framework with trajectory loss to reconstruct real samples by aligning the generator's output with the real data distribution. The process involves iterative optimization of synthetic datasets, training of auxiliary models, and use of diffusion processes to impose constraints on the generator. The attack relies on the synthetic dataset's implicit encoding of weight trajectories and leverages gradient descent dynamics to infer architecture and membership. The diffusion framework uses trajectory loss to guide the generator toward the real data distribution by exploiting information embedded in the synthetic dataset. The method combines model training, loss trajectory analysis, and generative modeling to achieve its goals.  
DOMAIN: machine learning privacy attacks  
STRUCTURE: other: iterative model training  
DATA_OBJECT: set or table  
INFERENCE: deterministic or closed-form  
PROBLEM_FORM: inference  
DISTRIBUTION: none  
COMPLEXITY: not stated  
DATA_AVAILABILITY: none  
CODE_AVAILABILITY: on-request  
PREREGISTRATION: none  
EVIDENCE_BASIS: empirical-with-private-data
