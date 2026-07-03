MECHANISM: The paper computes a biomechanically informed image registration framework that integrates finite element simulation with deformable image registration to track anatomical deformation. The process begins by segmenting a structure from imaging data to create a mesh-based model. Material properties and boundary conditions are applied to simulate deformation from an open to a closed configuration, generating intermediate states that approximate the structure's movement between time frames. These simulated states are then used as prior knowledge in a registration pipeline to align anatomical features across images, correcting deviations caused by modeling assumptions. The registration step propagates segmentation from an initial frame to subsequent frames, ensuring alignment with patient-specific imaging data. Strain is computed by comparing deformation across time points, using metrics such as areal, Green-Lagrange, and deviatoric strains. The method relies on deterministic modeling of material behavior and does not incorporate probabilistic uncertainty. The simulation uses a hyperelastic constitutive model to capture nonlinear deformation, with parameters calibrated to physiological data. The registration process iteratively adjusts model geometry to match observed image data, improving tracking accuracy. The framework is evaluated across multiple imaging modalities and patient cohorts to validate its ability to quantify strain and deformation.  
DOMAIN: biomedical engineering  
STRUCTURE: other: finite element method  
DATA_OBJECT: mesh  
INFERENCE: deterministic or closed-form  
PROBLEM_FORM: estimation  
DISTRIBUTION: none  
COMPLEXITY: not stated  
DATA_AVAILABILITY: none  
CODE_AVAILABILITY: none  
PREREGISTRATION: none  
EVIDENCE_BASIS: empirical-with-private-data
