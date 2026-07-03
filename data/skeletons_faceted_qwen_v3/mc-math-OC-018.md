MECHANISM: This paper computes tight bounds on distributionally robust risk (DR risk) and generalization complexity using geometric properties of loss growth functions. The method constructs least concave and star-shaped majorants of individual and maximal rate functions, which quantify how loss values change under localized perturbations. The algorithm proceeds by (1) defining a rate function Δθ(z,t) as the supremum of loss differences over all data points within distance t from z, (2) deriving empirical maximal rates across the dataset, (3) constructing lower and upper bounds on DR risk via the average of star-shaped majorants and concave majorants of these rates, and (4) extending these bounds to adversarial Rademacher complexity by replacing standard loss functions with their worst-case perturbations. The framework avoids requiring Lipschitz continuity, differentiability, or bounded domains, and applies to both finite and infinite Wasserstein exponents. It also introduces an adversarial score relaxation for practical computation in deep learning, enabling layer-wise analysis by composing concave majorants through product and composition maps. Theoretical guarantees include conditions for finite DR risk, existence of robust classifiers, and elimination of dependencies on network depth, width, and input diameter in complexity bounds.  
DOMAIN: machine learning and robust optimization  
STRUCTURE: other: geometric framework for risk analysis  
DATA_OBJECT: continuous function or field  
INFERENCE: deterministic or closed-form  
PROBLEM_FORM: estimation  
DISTRIBUTION: none  
COMPLEXITY: not stated  
DATA_AVAILABILITY: public-benchmark-used  
CODE_AVAILABILITY: none  
PREREGISTRATION: none  
EVIDENCE_BASIS: empirical-with-released-data
