MECHANISM: The paper computes electronic and structural properties of materials by solving the Kohn-Sham equations derived from density functional theory (DFT). The process begins by defining an effective potential that includes exchange-correlation effects, which are approximated using different functional forms (e.g., PBE, SCAN, HSE06). The Kohn-Sham equations are solved iteratively to obtain eigenvalues and eigenfunctions representing the electronic structure. Structural properties are determined by optimizing lattice parameters through energy minimization until forces on atoms are below a threshold. Band structures and density of states are calculated by sampling the Brillouin zone with a k-grid and projecting electronic states onto atomic orbitals. Results are benchmarked against experimental data and compared to outcomes from many-body perturbation theory (MBPT) calculations, specifically the $GW_0$ method, to assess accuracy. Spin-orbit coupling effects are incorporated as a post-scf correction. The computational workflow involves solving large-scale eigenvalue problems, optimizing geometries, and analyzing electronic properties through band gap and density of states calculations. The choice of exchange-correlation functional significantly influences the accuracy of predicted structural and electronic properties, with SCAN showing superior performance relative to PBE and HSE06 in this study.  
DOMAIN: computational materials science  
STRUCTURE: dense linear algebra  
DATA_OBJECT: grid or lattice  
INFERENCE: deterministic or closed-form  
PROBLEM_FORM: estimation  
DISTRIBUTION: none  
COMPLEXITY: not stated  
DATA_AVAILABILITY: none  
CODE_AVAILABILITY: public-repository  
PREREGISTRATION: none  
EVIDENCE_BASIS: empirical-with-released-data
