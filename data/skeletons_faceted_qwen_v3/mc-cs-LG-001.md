MECHANISM: The paper computes a parameter-efficient fine-tuning method for neural networks by introducing low-rank matrices to adjust pre-trained model weights. The process begins with initializing a base model trained on a dataset with less accurate but broader ground truth. A low-rank adapter network is then added to specific layers of the model, where the adapter matrices have a rank significantly smaller than the original weight matrices. These adapters are trained using a loss function that measures the deviation between predicted and ground truth values, with the loss function designed to prioritize minimizing bias and scatter in the output. During training, the adapters modify the model's parameters without retraining the entire base model, allowing for efficient updates with minimal computational overhead. The method is applied iteratively across multiple epochs, with early stopping criteria based on validation loss. The final model combines the base model's generalization capabilities with the fine-tuned adapters' ability to adapt to new ground truth data. The approach is compared against traditional transfer learning and full retraining, with performance evaluated using metrics such as bias, scatter, and outlier rates. The method's effectiveness is demonstrated through experiments on galaxy image datasets, where it achieves lower bias and scatter than traditional transfer learning while requiring less computational time than full retraining. The adapters are applied uniformly across all layers, enabling the model to retain knowledge from the base dataset while adapting to new data. The loss function is optimized using gradient descent with a learning rate scheduler, and the final model's parameters are a combination of the base model's weights and the low-rank adapters' adjustments.  
DOMAIN: astrophysics, photometric redshift estimation  
STRUCTURE: other: parameter-efficient fine-tuning  
DATA_OBJECT: grid or lattice  
INFERENCE: deterministic or closed-form  
PROBLEM_FORM: estimation  
DISTRIBUTION: continuous; continuous  
COMPLEXITY: not stated  
DATA_AVAILABILITY: dataset-with-DOI-or-handle  
CODE_AVAILABILITY: public-repository  
PREREGISTRATION: none  
EVIDENCE_BASIS: empirical-with-released-data
