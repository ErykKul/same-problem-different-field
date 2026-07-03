MECHANISM: The paper computes a lightweight neural radiance field (NeRF) model optimized for ultra-low-power microcontroller units (MCUs) aboard nano-drones. The model uses a multi-resolution hash-grid positional encoding to map 3D spatial coordinates to high-dimensional feature vectors, reducing memory usage through parameter tuning of hash table size and batch dimensions. A density multi-layer perceptron (MLP) predicts volume density and hidden features from encoded positions, while a separate color MLP generates emitted color from hidden features and encoded view directions. Training involves sampling rays through random pixels, aggregating sample colors and densities via volume rendering, and optimizing a Huber loss with Adam. To fit resource constraints, the model reduces batch size, input resolution, and hash table parameters, while employing tiling strategies to manage memory transfers on the GAP9 MCU. Federated learning is implemented by distributing training across a swarm of drones, where each drone trains on local data and periodically shares model updates with a coordinator, which aggregates parameters using FedAvg. The coordinator broadcasts the global model to all drones, enabling collaborative learning without exchanging raw data. Memory locality is prioritized through L1 cache tiling and asynchronous DMA transfers, ensuring compute-bound execution on the multi-core GAP9. The final model achieves a 96% reduction in memory footprint compared to Instant-NGP while maintaining acceptable reconstruction accuracy.  
DOMAIN: computer vision and robotics  
STRUCTURE: other: neural network with hash encoding  
DATA_OBJECT: grid or lattice  
INFERENCE: deterministic or closed-form  
PROBLEM_FORM: estimation  
DISTRIBUTION: continuous; continuous  
COMPLEXITY: not stated  
DATA_AVAILABILITY: none  
CODE_AVAILABILITY: none  
PREREGISTRATION: none  
EVIDENCE_BASIS: empirical-with-private-data
