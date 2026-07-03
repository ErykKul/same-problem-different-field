MECHANISM: A learning-based approach synthesizes stochastic barrier functions for finite-time safety certification of systems with unknown disturbance distributions. Given a continuous deterministic system with stochastic disturbances, the method learns safety guarantees from i.i.d. disturbance samples without assuming Lipschitz continuity on dynamics. Safety is formulated as a chance-constrained problem: design a barrier function ensuring trajectories remain within a safe region with high probability. Scenario optimization solves barrier function synthesis over finite disturbance samples generating candidate solutions. Probably approximately correct (PAC) analysis quantifies confidence via VC dimension and Rademacher complexity, establishing sample-complexity bounds for certified safety. The approach handles general nonlinear systems without requiring piecewise affine approximations or structural restrictions on barrier function form.
DOMAIN: Stochastic control safety certification with unknown disturbances
STRUCTURE: optimization only
DATA_OBJECT: dense matrix or tensor
INFERENCE: sampling or Monte-Carlo
PROBLEM_FORM: decision or test
DISTRIBUTION: none
COMPLEXITY: finite-sample bound
