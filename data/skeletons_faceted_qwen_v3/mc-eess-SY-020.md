MECHANISM: The paper computes a dynamical system modeling RNA velocity through ordinary differential equations (ODEs) that couple unspliced and spliced RNA concentrations with gene regulatory networks (GRNs) and spatial consensus terms. The system is defined by two ODEs per gene and cell, where unspliced RNA $u$ evolves based on a rational function of spliced RNA $s$ and regulatory matrices $W^+$ and $W^-$, while spliced RNA $s$ incorporates a consensus term involving intercellular communication. The model includes equilibrium analysis, stability conditions via Lyapunov functions, and optimal control strategies for interventions. The rational function $R_g(s)$ aggregates positive and negative regulatory effects, and stability depends on parameters like splicing rates $\beta$, degradation rates $\gamma$, and the spectral radius of a matrix derived from $\gamma^{-1}\alpha W^+$. The analysis extends to spatially coupled networks by adding consensus terms proportional to differences in spliced RNA across cells. The paper derives sufficient conditions for equilibrium existence and global asymptotic stability, involving inequalities between $\alpha$, $\beta$, $\gamma$, and network parameters. Control-theoretic approaches are used to design minimum-time interventions for gene knockouts or drugs, framed as optimal control problems.  
DOMAIN: gene regulatory networks and RNA velocity  
STRUCTURE: other: ordinary differential equations  
DATA_OBJECT: continuous function or field  
INFERENCE: deterministic or closed-form  
PROBLEM_FORM: simulation or generation  
DISTRIBUTION: none  
COMPLEXITY: convergence rate  
DATA_AVAILABILITY: none  
CODE_AVAILABILITY: none  
PREREGISTRATION: none  
EVIDENCE_BASIS: mathematical-proof
