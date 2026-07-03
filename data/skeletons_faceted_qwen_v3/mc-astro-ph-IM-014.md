MECHANISM: The paper computes the turbulence driving parameter $b$ by isolating turbulent contributions from simulation data. It applies a low-pass Gaussian filter to density, velocity, and magnetic field fields to remove non-turbulent components like large-scale shear and vertical stratification. Turbulent density fluctuations are derived by subtracting the smoothed field from the original field, then computing the standard deviation of the resulting turbulent density field. The turbulent sonic Mach number is calculated as the root sum of squares of standard deviations of velocity components divided by the sound speed. Plasma $\beta$ is determined from the ratio of thermal to magnetic pressure, with the magnetic field filtered similarly. These quantities are combined via a mathematical relationship to solve for $b$, which quantifies the ratio of solenoidal to compressive turbulence modes. The method involves spatial filtering, statistical moment calculations, and algebraic transformations of field data. Time evolution of $b$, Mach number, and $\beta$ is analyzed across simulation snapshots. Correlations between these parameters and star formation rates are assessed using statistical measures. The process is deterministic, relying on simulation outputs and mathematical equations without probabilistic modeling.
DOMAIN: astrophysical turbulence in interstellar medium
STRUCTURE: other: simulation-based analysis
DATA_OBJECT: grid or lattice
INFERENCE: deterministic or closed-form
PROBLEM_FORM: estimation
DISTRIBUTION: none
COMPLEXITY: not stated
DATA_AVAILABILITY: dataset-with-DOI-or-handle
CODE_AVAILABILITY: public-repository
PREREGISTRATION: none
EVIDENCE_BASIS: simulation-study
