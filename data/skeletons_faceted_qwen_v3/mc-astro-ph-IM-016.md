MECHANISM: The paper computes a dual-domain error correction algorithm to bound reconstruction errors in both spatial and frequency representations of data. Given a base compressor's output and user-defined error bounds in both domains, the algorithm first transforms spatial errors into frequency errors using the discrete Fourier transform (DFT). Frequency errors are expressed as linear combinations of spatial errors with complex coefficients, enabling the derivation of a feasible region defined by the intersection of two geometric constraints: an axis-aligned hypercube (s-cube) from spatial error bounds and a rotated hypercube (f-cube) from frequency error bounds. The algorithm iteratively projects the spatial error vector onto the s-cube and f-cube, alternating between domains until the error vector lies within their intersection. Each projection step involves clipping values exceeding bounds in the respective domain, followed by an inverse transform to return to the original domain. The process ensures that errors in both domains are simultaneously constrained without requiring explicit knowledge of the data's structure. After convergence, the algorithm quantizes and compresses the adjustments made to the spatial error vector, reducing storage overhead. The method relies on the mathematical properties of the DFT and the POCS (Projections Onto Convex Sets) iterative technique, which guarantees convergence to a feasible solution when the intersection of constraints is non-empty. The algorithm is implemented in parallel on GPUs to accelerate projections and constraint checks across data blocks. The final output preserves both spatial and frequency fidelity by ensuring the adjusted data meets the user-specified error bounds in both domains.  
DOMAIN: scientific data compression  
STRUCTURE: iterative optimization  
DATA_OBJECT: dense vector  
INFERENCE: deterministic or closed-form  
PROBLEM_FORM: optimization  
DISTRIBUTION: none  
COMPLEXITY: polynomial iterative  
DATA_AVAILABILITY: dataset-with-DOI-or-handle  
CODE_AVAILABILITY: public-repository  
PREREGISTRATION: none  
EVIDENCE_BASIS: empirical-with-released-data
