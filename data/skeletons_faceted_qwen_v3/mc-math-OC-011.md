MECHANISM: The paper computes stability conditions for decentralized vehicular admission control (VAC) schemes in traffic networks with nonlinear dynamics and bounded uncertainty. It models traffic as a network of regions with density, flow, and speed variables, where each region's flow is described by a concave macroscopic fundamental diagram (MFD) with uncertainty terms. The VAC dynamics are defined as nonlinear functions of regional density, with control variables determining admitted vehicle inflow. Using passivity theory, the paper derives distributed, locally verifiable conditions on VAC dynamics that ensure asymptotic stability under modeling uncertainty. These conditions are formulated as inequalities involving system states and control parameters, validated through numerical simulations on synthetic networks. The approach avoids global optimization, instead relying on local information exchange and robustness to MFD parameter variations. The analysis assumes Lipschitz continuity of MFD components and bounded uncertainty terms, ensuring that inter-regional flows remain non-negative and concave. The stability proof leverages passivity properties of the closed-loop system, demonstrating that energy dissipation guarantees convergence to equilibrium points. The method is applicable to arbitrary connected network topologies and scales to large systems without recalibration.  
DOMAIN: urban traffic control  
STRUCTURE: other: passivity-based control  
DATA_OBJECT: graph or network  
INFERENCE: deterministic or closed-form  
PROBLEM_FORM: proof or characterization  
DISTRIBUTION: none  
COMPLEXITY: not stated  
DATA_AVAILABILITY: none  
CODE_AVAILABILITY: none  
PREREGISTRATION: none  
EVIDENCE_BASIS: simulation-study
