MECHANISM: The paper computes a three-stage algorithm for pruning a set of 3D Gaussians representing a scene. First, it filters Gaussians by projecting them onto a set of masked regions defined by sparse binary masks, retaining only those that project to any masked region across multiple views. Second, it validates the color of each retained Gaussian by comparing its rendered color against a depth-buffered reference from the masked image, discarding those with significant color mismatch. Third, it removes outliers by identifying Gaussians that are spatially distant from the scene center, far from their k nearest neighbors, or inconsistent across multiple views. The algorithm uses thresholds, statistical percentiles, and geometric proximity metrics to determine which Gaussians to retain or remove. It operates on a collection of Gaussians with position, covariance, opacity, and color attributes, and applies spatial and color-based criteria sequentially to reduce the set size while preserving target object structure. The method does not involve probabilistic modeling or optimization beyond threshold-based decisions. It relies on the consistency of sparse masks across views to guide pruning without requiring dense supervision. The final output is a pruned set of Gaussians representing the target object with reduced cardinality.  
DOMAIN: 3D reconstruction and semantic segmentation  
STRUCTURE: other: multi-stage filtering and validation  
DATA_OBJECT: set or table  
INFERENCE: deterministic or closed-form  
PROBLEM_FORM: optimization  
DISTRIBUTION: none  
COMPLEXITY: not stated  
DATA_AVAILABILITY: public-repository  
CODE_AVAILABILITY: public-repository  
PREREGISTRATION: none  
EVIDENCE_BASIS: empirical-with-released-data
