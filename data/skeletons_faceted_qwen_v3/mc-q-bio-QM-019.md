MECHANISM: The paper computes the dynamics of a network of coupled oscillators under external periodic forcing. The system is modeled using a set of ordinary differential equations (ODEs) with variables representing concentrations of mRNA, protein, and inhibitor. Each oscillator interacts via a mean-field coupling term derived from the average of a specific variable across all oscillators. The model incorporates both constant and periodic external inputs, simulating light-dark cycles. The system's behavior is analyzed by varying parameters such as coupling strength and the proportion of oscillators in different subgroups. The key computation involves simulating the system's response to parameter changes, decomposing the solution into stationary and oscillatory components, and identifying bifurcation points where the system transitions between free-running and entrained states. The analysis reveals that the transition occurs via a supercritical Hopf-like bifurcation, characterized by a discontinuous jump in the period of oscillations. The model predicts how the proportion of oscillators in different subgroups affects synchronization, showing that increasing the fraction of one subgroup can suppress free-running modes and enforce entrainment. The computation includes numerical integration of ODEs, Fourier analysis of oscillatory outputs, and parameter sweeps to map bifurcation thresholds. The results are validated by comparing simulations of small and large networks, confirming the robustness of the transition mechanism. The model's predictions are linked to biological observations of circadian rhythm entrainment, though the computation itself is abstracted from domain-specific details.

DOMAIN: biological oscillators and synchronization

STRUCTURE: other: ODE-based model

DATA_OBJECT: continuous function or field

INFERENCE: deterministic or closed-form

PROBLEM_FORM: simulation or generation

DISTRIBUTION: none

COMPLEXITY: not stated

DATA_AVAILABILITY: none

CODE_AVAILABILITY: none

PREREGISTRATION: none

EVIDENCE_BASIS: simulation-study
