MECHANISM: The paper computes a method for imputing missing scores in constructed-response tests using automated scoring technologies to enhance Item Response Theory (IRT)-based ability estimation. The process begins by training AI graders on a subset of manually graded responses, where the model learns to predict scores for constructed-response items. These trained models are then used to generate imputed scores for missing data points across test items. The imputed scores are integrated into an IRT framework, which estimates latent learner abilities by maximizing the likelihood of observed and imputed scores under the IRT model's assumptions. The method explicitly addresses sparse or heterogeneous data by leveraging the AI grader's ability to generalize across item types and response patterns. The computational pipeline includes data preprocessing, model training, score imputation, and iterative optimization of the IRT parameters. The accuracy of ability estimation is evaluated by comparing imputed results with ground-truth scores from a held-out validation set. The approach reduces manual grading workload by minimizing the number of responses requiring human evaluation while maintaining statistical fidelity in ability estimation. The method does not rely on traditional data augmentation techniques but instead uses the predictive power of AI graders to fill gaps in the score matrix. The IRT model assumes a logistic relationship between item parameters, ability, and the probability of achieving a score, which is optimized using maximum likelihood estimation. The AI grader's output is treated as a probabilistic imputation, with uncertainty propagated through the IRT framework to refine ability estimates.  
DOMAIN: education, ability estimation, constructed-response tests  
STRUCTURE: other: machine learning-based imputation  
DATA_OBJECT: sequence or time-series; set or table  
INFERENCE: deterministic or closed-form  
PROBLEM_FORM: estimation  
DISTRIBUTION: continuous; normal  
COMPLEXITY: not stated  
DATA_AVAILABILITY: none  
CODE_AVAILABILITY: none  
PREREGISTRATION: none  
EVIDENCE_BASIS: empirical-with-private-data
