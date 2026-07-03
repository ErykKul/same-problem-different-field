MECHANISM: The paper computes a personalized estimator for a target regression function by integrating a pre-trained black-box model. Given a set of labeled samples from the target domain, the method first retrieves covariate points according to a specified sampling rule. It then applies a local smoothing operation to the pre-trained model's predictions, truncating excessive local variation to enforce Hölder regularity around each point. A kernel-based estimator is constructed to approximate the bias between the smoothed pre-trained model and the true regression function. This bias-corrected estimate is combined with the pre-trained model's output to form a personalized estimator. Tuning parameters are selected via cross-validation on validation samples, minimizing the mean squared error on these samples. The method ensures robustness against adversarial pre-trained models by relying on local smoothing rather than direct parameter access. Theoretical analysis establishes that the estimator achieves the minimax optimal rate for nonparametric regression under mild conditions, leveraging the pre-trained model to reduce effective Hölder complexity. The approach guarantees no degradation in performance compared to target-only estimation, even when the pre-trained model is uninformative. The algorithm operates by querying the pre-trained model at retrieved covariate points and applying kernel smoothing to the residuals between observed responses and smoothed predictions. The final estimator adapts to the smoothness of the target function and the noise structure through parameter selection.  
DOMAIN: nonparametric regression and model personalization  
STRUCTURE: other: kernel-based nonparametric estimation  
DATA_OBJECT: function or field  
INFERENCE: frequentist point estimate  
PROBLEM_FORM: estimation  
DISTRIBUTION: continuous; continuous  
COMPLEXITY: minimax optimal rate  
DATA_AVAILABILITY: dataset-with-DOI-or-handle  
CODE_AVAILABILITY: none  
PREREGISTRATION: none  
EVIDENCE_BASIS: empirical-with-released-data
