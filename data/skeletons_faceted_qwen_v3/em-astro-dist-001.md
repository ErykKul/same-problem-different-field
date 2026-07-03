MECHANISM: The paper computes the gravitational evolution of dark matter particles in a cosmological simulation. Initial conditions are generated using second-order Lagrangian perturbation theory, which maps density fluctuations into particle positions. The simulation employs a TreePM algorithm to calculate pairwise gravitational forces between particles, integrating their trajectories over time. After simulation, halo and subhalo structures are identified using phase-space clustering algorithms, and merger trees are constructed by linking halos across time steps. Power spectra are computed by assigning particles to a grid, applying Fast Fourier Transform (FFT) to estimate density fluctuations, and combining results from multiple mesh resolutions to extend the range of measurable wavenumbers. The process involves correcting for aliasing effects and normalizing particle weights to ensure consistency across different mesh scales. Halo mass functions are derived by counting halos above a minimum particle threshold and analyzing their distribution across mass and redshift. The simulation's accuracy is validated by comparing power spectra and mass functions against theoretical models and other simulations. No domain-specific terms are used; all entities are treated as abstract quantities or structures.  
DOMAIN: cosmological N-body simulation  
STRUCTURE: N-body or all-pairs  
DATA_OBJECT: point set  
INFERENCE: deterministic or closed-form  
PROBLEM_FORM: simulation or generation  
DISTRIBUTION: none  
COMPLEXITY: not stated  
DATA_AVAILABILITY: dataset-with-DOI-or-handle  
CODE_AVAILABILITY: none  
PREREGISTRATION: none  
EVIDENCE_BASIS: simulation-study
