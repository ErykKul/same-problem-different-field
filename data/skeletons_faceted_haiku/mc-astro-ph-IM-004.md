MECHANISM: Integrates ResNet34 backbone (global semantic feature extraction on RGB channels) with ASCModule (fine-grained luminance texture via depthwise dilated convolution and Squeeze-and-Excitation attention in parallel branches). Two branches feed into FusionBlock: 1x1 convolution for dimensionality reduction, depthwise separable convolution residual unit, lightweight ECA module for cross-channel dependencies, and dropout. Output processed by global average pooling, flattening, batch normalization, fully connected layer, softmax. Training uses staged ResNet freezing, Focal Loss for class imbalance, 10-fold cross-validation.
DOMAIN: Cloud coverage classification, astronomical site testing
STRUCTURE: other: multi-branch convolutional neural network with fusion
DATA_OBJECT: dense matrix or tensor
INFERENCE: optimization only
PROBLEM_FORM: prediction or classification
DISTRIBUTION: none
COMPLEXITY: not stated
