MECHANISM: The paper computes a matrix-level optimization algorithm that enforces spectral constraints on weight matrices during training. It begins by initializing weight matrices to satisfy a target spectral norm $S = \sqrt{n_\ell/n_{\ell-1}}$, either through μP initialization or explicit normalization. The algorithm then projects gradient updates onto subspaces orthogonal to the top singular vectors of the weight matrix, ensuring that the spectral norm of the updated matrix remains equal to $S$. This projection is achieved by solving a constrained optimization problem where the update $\Delta$ must satisfy $\|\mathbf{W} - \eta S \Delta\| = S$, with $\Delta$ constrained to lie in the orthogonal complement of the top singular subspace. The solution to this problem is obtained by computing the singular value decomposition (SVD) of the projected gradient matrix and selecting the optimal $\Delta$ as the product of the left and right singular vectors of the projected gradient. The algorithm avoids explicit spectral normalization of weights by leveraging the structure of the projection, ensuring that the spectral norm remains stable across training steps. For large matrices, the method incorporates adaptive adjustments to maintain the spectral condition when the gap between the top and second singular values becomes small. The approach is designed to preserve μP-compatible scaling behavior while reducing computational overhead compared to prior methods that required repeated spectral normalization. The algorithm is formalized as a variant of Muon, named Muon++, which applies these principles to matrix updates without modifying the weight matrices directly. The method is analyzed theoretically to guarantee that the spectral conditions hold throughout training, and its practical implementation is validated through empirical studies on large language models.

DOMAIN: machine learning optimizers

STRUCTURE: other: constrained optimization

DATA_OBJECT: matrix

INFERENCE: deterministic or closed-form

PROBLEM_FORM: optimization

DISTRIBUTION: none

COMPLEXITY: not stated

DATA_AVAILABILITY: none

CODE_AVAILABILITY: none

PREREGISTRATION: none

EVIDENCE_BASIS: mathematical-proof
