MECHANISM: A lightweight neural radiance field model (Tiny-DroNeRF) compresses the Instant-NGP architecture for embedded deployment on resource-constrained MCUs. Hyperparameter optimization reduces network parameters and grid resolution while maintaining reconstruction fidelity (PSNR). The method uses multiresolution hash-grid positional encoding with efficient memory layouts enabling good cache locality. A federated learning scheme enables distributed training across multiple nano-drones: each drone trains locally on its captured images, then sends model updates (not raw images) to a coordinator which aggregates updates and redistributes the global model. Local training proceeds via standard gradient descent; communication occurs every 1000 steps with model parameters transmitted. The approach reconstructs 3D scenes and enables novel view synthesis despite individual drones having limited image coverage.
DOMAIN: Neural radiance fields for resource-constrained embedded systems and federated learning
STRUCTURE: other: lightweight neural representation with federated aggregation
DATA_OBJECT: dense matrix or tensor
INFERENCE: sampling or Monte-Carlo
PROBLEM_FORM: simulation or generation
DISTRIBUTION: continuous
COMPLEXITY: polynomial iterative
