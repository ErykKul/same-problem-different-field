MECHANISM: A bipartite associative memory network with visible and hidden neurons uses a Heaviside step function (threshold nonlinearity) to enable distributed representations. The system evolves via coupled differential equations: visible neurons integrate weighted hidden-neuron states; hidden neurons integrate weighted visible-neuron states. Fixed points correspond to stable memory patterns in the hidden layer. All 2^Nh binary patterns of hidden units become stable fixed points when Nv >> Nh, because the weight matrix J approaches the identity matrix. A learning rule optimizes synaptic weights and threshold to store target memories, enabling compositional memory storage. Basin of attraction analysis shows robustness to noise proportional to sqrt(Nv/Nh). Numerical validation on MNIST and CIFAR-10 demonstrates high-capacity recall and structured latent representations.
DOMAIN: Associative memory, computational neuroscience, neural networks
STRUCTURE: sparse linear algebra
DATA_OBJECT: graph or network
INFERENCE: deterministic or closed-form
PROBLEM_FORM: estimation
DISTRIBUTION: none
COMPLEXITY: not stated
