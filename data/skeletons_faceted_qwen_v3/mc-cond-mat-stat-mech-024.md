MECHANISM: The paper computes the longitudinal-field fidelity susceptibility $\chi^{(h)}_F$ to detect criticality in quantum spin systems. The process begins by constructing the Hamiltonian matrix for the $J_1$-$J_2$ transverse-field Ising model, which includes terms for nearest-neighbor interactions, next-nearest-neighbor interactions, transverse and longitudinal fields, and the absolute value of the magnetic moment. The ground state is obtained via exact diagonalization (ED), which explicitly computes the eigenvalues and eigenvectors of the Hamiltonian. The fidelity $F$ is calculated as the overlap between ground states under perturbations of the longitudinal field $H$. The susceptibility $\chi^{(h)}_F$ is derived by taking the second derivative of $F$ with respect to $H$ at $H=0$, scaled by the system size $N$. The modified susceptibility is then analyzed using finite-size scaling, where the critical point is estimated by fitting the scaling form $\chi^{(h)}_F = L^{x_F} f((\Gamma - \Gamma_c)L^{1/\nu})$, with $x_F$ determined by critical exponents $\nu$, $\gamma_F$, and $z$. The method is extended to multi-criticality by introducing a scaling parameter $\eta = 0.5 - J_2$ and adjusting the scaling function to include $\eta L^{\phi/\dot{\nu}}$. The $\beta$-function is computed from the scaling behavior of $\chi^{(h)}_F$ and compared to the magnetic susceptibility $\chi$ to validate the critical exponents. All computations rely on deterministic, closed-form evaluations of matrix eigenvalues and derivatives, without probabilistic or statistical inference.  
DOMAIN: quantum spin systems  
STRUCTURE: dense linear algebra  
DATA_OBJECT: dense matrix  
INFERENCE: deterministic or closed-form  
PROBLEM_FORM: simulation or generation  
DISTRIBUTION: none  
COMPLEXITY: not stated  
DATA_AVAILABILITY: none  
CODE_AVAILABILITY: none  
PREREGISTRATION: none  
EVIDENCE_BASIS: simulation-study
