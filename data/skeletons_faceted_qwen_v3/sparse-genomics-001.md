MECHANISM: The paper computes a weighted L1-penalized regression to select features from multiple data modalities. The method minimizes a loss function that combines a prediction error term (sum of squared residuals for linear models, or equivalent for logistic/Cox models) with a penalty term that applies distinct scaling factors to each modality's coefficients. The penalty factors are determined either through cross-validation or user-specified values. Variables are standardized before applying the penalty, which is implemented as a rescaling of the input matrix. The optimization problem is solved using standard LASSO algorithms with adjusted penalty parameters. The method allows for different modality-specific shrinkage of coefficients, favoring modalities with higher relevance by reducing their penalty. The solution path is computed iteratively over a grid of penalty values, with model selection based on cross-validated prediction performance metrics. The approach generalizes to binary, time-to-event, and continuous outcomes by substituting the loss function accordingly. The final model selects variables by thresholding coefficients toward zero, producing sparse predictions that balance model fit and penalty cost.  
DOMAIN: biomedical data integration  
STRUCTURE: sparse linear algebra  
DATA_OBJECT: matrix  
INFERENCE: deterministic or closed-form  
PROBLEM_FORM: prediction or classification  
DISTRIBUTION: binary; logistic  
COMPLEXITY: not stated  
DATA_AVAILABILITY: dataset-with-DOI-or-handle  
CODE_AVAILABILITY: public-repository  
PREREGISTRATION: none  
EVIDENCE_BASIS: simulation-study
