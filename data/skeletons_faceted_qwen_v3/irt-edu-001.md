MECHANISM: The paper computes a method for estimating latent ability from incomplete score data by combining automated scoring models with item response theory (IRT). First, a model is trained on a subset of scored responses to predict missing scores, using either fine-tuned neural networks or zero-shot large language models. The model's predictions are then used to generate a complete dataset. Next, IRT models are applied to estimate latent ability parameters by maximizing the likelihood of observed scores, which are defined as probabilistic functions of ability and item characteristics. The IRT model assumes that each score observation follows a parametric distribution determined by item parameters and the latent ability of the entity. The method avoids explicitly modeling underlying data patterns by directly using raw response text for prediction. The imputation step is deterministic, relying on the trained model's output, while the ability estimation step involves iterative optimization to find maximum likelihood parameters. The process is repeated across multiple missing data configurations to evaluate robustness under varying sparsity levels. The final ability estimates are compared to gold-standard values using normalized root-mean-squared error and correlation coefficients. The method is designed to handle heterogeneous data without assuming a single data-generation process.  
DOMAIN: educational assessment and statistical modeling  
STRUCTURE: other: machine learning and probabilistic modeling  
DATA_OBJECT: matrix with missing entries  
INFERENCE: frequentist point estimate  
PROBLEM_FORM: estimation  
DISTRIBUTION: ordinal; probabilistic  
COMPLEXITY: not stated  
DATA_AVAILABILITY: public-benchmark-used  
CODE_AVAILABILITY: none  
PREREGISTRATION: none  
EVIDENCE_BASIS: empirical-with-released-data
