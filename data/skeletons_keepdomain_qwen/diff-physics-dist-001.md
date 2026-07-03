MECHANISM: The paper computes electronic structure properties of cesium-based materials using density functional theory (DFT) with three exchange-correlation functionals (PBE, SCAN, HSE06). The method involves solving the Kohn-Sham equations to calculate the total energy, lattice parameters, and band structure of bulk Cs3Sb and Cs2Te. Each functional's performance is evaluated by comparing predicted structural parameters (unit cell volume) and electronic properties (band gap) against experimental data. Spin-orbit coupling effects are incorporated to assess their impact on valence band splitting and band-gap reduction. The computational workflow includes setting up initial crystal structures, applying periodic boundary conditions, and performing self-consistent field iterations to converge the electronic density. The accuracy of each functional is quantified by statistical metrics such as mean absolute error for lattice parameters and band gap deviations. The analysis emphasizes trade-offs between computational cost (e.g., HSE06's higher expense vs. SCAN's efficiency) and predictive accuracy. The method does not involve sampling or probabilistic inference but relies on deterministic solutions to the DFT equations. The results are validated through comparison with experimental measurements and theoretical benchmarks. The paper concludes that SCAN provides the best balance between accuracy and computational efficiency for these materials.
DOMAIN: materials science and electronic structure
STRUCTURE: dense linear algebra
DATA_OBJECT: grid or lattice
INFERENCE: deterministic or closed-form
PROBLEM_FORM: estimation
DISTRIBUTION: continuous; continuous
COMPLEXITY: not stated
DATA_AVAILABILITY: none
CODE_AVAILABILITY: none
PREREGISTRATION: none
EVIDENCE_BASIS: simulation-study
