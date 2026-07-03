MECHANISM: The paper computes quantitative prediction of constituent concentrations in aluminum standard alloys using laser-induced breakdown spectroscopy (LIBS) data. The process involves collecting LIBS spectra from aluminum samples, preprocessing the spectral data to remove noise and normalize intensities, selecting relevant spectral features, and training two linear machine learning models: support vector regression (SVR) with a radial basis function kernel and multiple linear regression (MLR). The models are trained on a dataset of LIBS spectra paired with known concentrations of aluminum alloys. Feature importance is analyzed to identify which wavelengths contribute most to prediction accuracy. The models are validated using cross-validation, and their performance is evaluated using metrics such as root mean square error (RMSE) and coefficient of determination (R²). The SVR model is tuned by optimizing hyperparameters like the kernel coefficient and regularization parameter. Both models are compared based on their predictive accuracy and robustness to variations in LIBS signal quality. The computational pipeline is implemented using standard machine learning libraries, with no novel algorithmic contributions beyond the application of existing regression techniques to LIBS data.
DOMAIN: quantitative analysis in laser-induced breakdown spectroscopy
STRUCTURE: dense linear algebra
DATA_OBJECT: dense matrix
INFERENCE: deterministic or closed-form
PROBLEM_FORM: prediction or classification
DISTRIBUTION: none
COMPLEXITY: not stated
DATA_AVAILABILITY: none
CODE_AVAILABILITY: none
PREREGISTRATION: none
EVIDENCE_BASIS: empirical-with-private-data
