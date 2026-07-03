MECHANISM: The paper computes a predictive model that integrates a quantitative regressor with symbolic reasoning to simulate and explain drug response mechanisms. The process begins with transforming high-dimensional transcriptomic data using principal component analysis to reduce noise and dimensionality. A regularized random forest regressor is trained on this transformed data, along with mutational and clinical metadata, to predict drug sensitivity (IC50). The model is validated using a zero-leakage pipeline to ensure statistical honesty. Inverse reasoning is enabled by treating the regressor as a deterministic simulator, allowing the computation of sensitivity deltas from hypothetical genomic perturbations. An autonomous large language model (LLM) agent queries this simulator to generate mechanistic explanations, mapping numerical changes to established biological pathways. The framework uses SHAP values for feature attribution but emphasizes symbolic reasoning to contextualize results within known molecular mechanisms. The model is tested on synthetic clinical data to confirm generalizability, using survival analysis to validate predicted drug response patterns. The integration of numerical prediction and symbolic explanation ensures both accuracy and interpretability in identifying therapeutic vulnerabilities and resistance mechanisms.
DOMAIN: precision oncology
STRUCTURE: other: neuro-symbolic integration
DATA_OBJECT: dense matrix or tensor
INFERENCE: deterministic or closed-form
PROBLEM_FORM: prediction or classification
DISTRIBUTION: continuous; normal
COMPLEXITY: not stated
DATA_AVAILABILITY: dataset-with-DOI-or-handle
CODE_AVAILABILITY: none
PREREGISTRATION: none
EVIDENCE_BASIS: empirical-with-released-data
