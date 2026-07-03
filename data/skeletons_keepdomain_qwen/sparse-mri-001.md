MECHANISM: The paper computes a parallel compressed sensing (CS) reconstruction model for dynamic contrast-enhanced MRI (DCE-MRI) that enforces flexible weighted sparsity constraints across both spatial and temporal dimensions. The method combines golden-angle radial sampling with parallel imaging to reduce motion artifacts while maintaining high resolution. A weighted ℓ₁-norm penalty is applied to the spatiotemporal signal, where weights are adaptively adjusted to balance spatial and temporal sparsity contributions. The reconstruction problem is formulated as a convex optimization with a fidelity term enforcing data consistency and a regularization term enforcing sparsity. A fast thresholding algorithm is derived by solving the proximal operator of the weighted ℓ₁-norm, which is proven to converge in finite steps. The algorithm iteratively updates the image estimate by applying soft-thresholding to the weighted gradient domain. The method is evaluated on in vivo liver DCE-MRI datasets with accelerated undersampling, comparing reconstruction quality against existing CS and parallel imaging techniques. The weights are determined based on prior knowledge of tissue dynamics and spatial coherence, allowing the model to prioritize temporal sparsity in regions with rapid contrast uptake and spatial sparsity in stable regions. The thresholding step is optimized for parallel computation to reduce overall reconstruction time. The model's performance is validated using quantitative metrics such as root mean square error and structural similarity index.  
DOMAIN: medical imaging and signal processing  
STRUCTURE: sparse linear algebra  
DATA_OBJECT: grid or lattice  
INFERENCE: deterministic or closed-form  
PROBLEM_FORM: estimation  
DISTRIBUTION: none  
COMPLEXITY: polynomial iterative  
DATA_AVAILABILITY: none  
CODE_AVAILABILITY: none  
PREREGISTRATION: none  
EVIDENCE_BASIS: empirical-with-private-data
