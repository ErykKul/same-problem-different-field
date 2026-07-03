MECHANISM: The paper computes a hierarchical numerical solver for linear systems derived from integral equations by replacing classical relaxation methods with neural operators. The algorithm first discretizes the integral equation into a linear system $A\mathbf{x} = \mathbf{y}$, where $A$ is a dense matrix with Toeplitz structure. Neural operators are trained offline to approximate solution mappings for this system. Each neural smoother is trained independently on a grid level using a level-wise loss function that incorporates spectral filtering to target high-frequency error components. The loss function minimizes the residual of the preconditioned system, ensuring that each neural smoother focuses on resolving distinct spectral bands. During inference, the neural smoothers replace classical relaxation steps in a multigrid cycle, which alternates between smoothing on fine grids and coarse-grid correction. The method avoids the need for preconditioning matrices by leveraging the spectral properties of the neural operators. The multigrid cycle is implemented as a V-cycle, with pre-smoothing steps on each grid level followed by restriction to coarser grids, exact solving on the coarsest grid, and post-smoothing interpolation back to finer grids. The training process uses a data-driven approach, minimizing the squared error between predicted and true solutions over a set of generated training samples. The algorithm generalizes to varying problem sizes and regularization weights without retraining.  
DOMAIN: computational mathematics and machine learning  
STRUCTURE: structured grid  
DATA_OBJECT: dense matrix  
INFERENCE: deterministic or closed-form  
PROBLEM_FORM: estimation  
DISTRIBUTION: none  
COMPLEXITY: not stated  
DATA_AVAILABILITY: none  
CODE_AVAILABILITY: none  
PREREGISTRATION: none  
EVIDENCE_BASIS: empirical-with-private-data
