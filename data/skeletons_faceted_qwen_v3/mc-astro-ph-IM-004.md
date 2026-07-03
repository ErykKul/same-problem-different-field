MECHANISM: The paper computes a deep neural network for image classification. Input images are first converted into a luminance map using a standard formula. Two parallel branches process the input: one extracts global semantic features using a ResNet34 backbone, while the other captures fine-grained texture features via an ASCModule with depthwise dilated convolutions and Squeeze-and-Excitation attention. Branch outputs are fused through a FusionBlock, which reduces channel dimensions, applies depthwise separable convolutions, integrates cross-channel dependencies with an ECA module, and applies dropout for regularization. Final features are pooled, normalized, and passed through a fully connected layer with softmax to produce class probabilities. Training uses Focal Loss with class weights to address imbalance, and a staged freezing strategy adapts the ResNet backbone for minority classes. The model's architecture balances global and local feature extraction, enhancing discriminability for low-light nighttime images.  
DOMAIN: astronomical image classification  
STRUCTURE: other: neural network with parallel branches and fusion  
DATA_OBJECT: dense matrix or tensor  
INFERENCE: deterministic or closed-form  
PROBLEM_FORM: classification  
DISTRIBUTION: none  
COMPLEXITY: not stated  
DATA_AVAILABILITY: none  
CODE_AVAILABILITY: none  
PREREGISTRATION: none  
EVIDENCE_BASIS: empirical-with-private-data
