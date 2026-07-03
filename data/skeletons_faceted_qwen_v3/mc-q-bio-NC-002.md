MECHANISM: The paper introduces a two-layer network with visible and hidden neurons, where the hidden layer uses a threshold nonlinearity to enable distributed representations. The dynamics are governed by differential equations for visible and hidden neuron states, with the hidden neurons' activation determined by a Heaviside step function applied to a weighted sum of visible neuron activities. The synaptic weights are initialized randomly from a Gaussian distribution and adjusted via an optimization procedure to minimize the difference between target memories and the network's stable fixed points. The threshold parameter is chosen to ensure all binary patterns of hidden neurons are stable, leading to exponential storage capacity. The model's stability is analyzed by showing that the weight matrix approaches the identity matrix when the number of visible neurons is much larger than hidden neurons, decoupling hidden neurons and allowing each to independently encode memory components. The learning rule involves minimizing a loss function that compares target memories to the network's reconstructed states, using a thresholded activation function approximated by a sigmoid for gradient-based training. The model demonstrates robustness to noise by showing that the basins of attraction for fixed points are large, even with additive noise in the visible units. The hidden layer's low dimensionality preserves class-discriminative structure, enabling efficient decoding of complex patterns through combinations of hidden neuron activations. Theoretical analysis and numerical simulations confirm the exponential capacity and stability of the network's fixed points.  
DOMAIN: neural networks  
STRUCTURE: other: dynamic system  
DATA_OBJECT: dense matrix  
INFERENCE: deterministic or closed-form  
PROBLEM_FORM: simulation or generation  
DISTRIBUTION: none  
COMPLEXITY: not stated  
DATA_AVAILABILITY: public-benchmark-used  
CODE_AVAILABILITY: none  
PREREGISTRATION: none  
EVIDENCE_BASIS: empirical-with-released-data
