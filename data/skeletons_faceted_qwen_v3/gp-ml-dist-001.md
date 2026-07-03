MECHANISM: The paper computes a modified convolutional neural network (CNN) architecture with a minimum distance network (MDN) classifier. The CNN extracts features through convolutional layers, pooling operations, and ReLU activations, reducing input dimensionality while preserving spatial hierarchies. The MDN classifier replaces the fully connected layer, using a fixed Walsh matrix to represent class centers. During training, the CNN is optimized to map input feature vectors to rows/columns of the Walsh matrix, minimizing the mean squared error between the feature extractor's output and the Walsh vectors. The divergence value, calculated as the trace of the inverse within-class scatter matrix multiplied by the between-class scatter matrix, is maximized to enhance class separability. The Walsh matrix's structure ensures maximal Hamming distances between class centers, improving classification performance. Training focuses on the CNN, with the MDN's weights fixed during training and only used during testing. The method avoids backpropagation through the MDN by predefining class centers, reducing hyperparameter complexity and computational load. The approach is tested on diverse datasets, including ECG, EEG, and image data, with validation through empirical performance comparisons.  
DOMAIN: deep learning  
STRUCTURE: structured grid  
DATA_OBJECT: dense matrix or tensor  
INFERENCE: deterministic or closed-form  
PROBLEM_FORM: classification  
DISTRIBUTION: none  
COMPLEXITY: not stated  
DATA_AVAILABILITY: public-benchmark-used  
CODE_AVAILABILITY: none  
PREREGISTRATION: none  
EVIDENCE_BASIS: empirical-with-released-data
