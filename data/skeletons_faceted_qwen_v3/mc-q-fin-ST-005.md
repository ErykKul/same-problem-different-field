MECHANISM: The paper computes a unified representation of heterogeneous financial data through a shared transformer-based backbone and modular task heads. Input modalities (textual, numerical, visual, and graph-based) are encoded separately using domain-specific encoders (e.g., temporal attention for time series, graph attention networks for relational structures). These encodings are projected into a shared semantic embedding space via cross-modal alignment mechanisms, including contrastive learning. Task-specific heads then extract features for micro-level stock prediction, macro-level systemic risk assessment, and policy analysis. For stock prediction, an autoregressive decoder generates future price trajectories conditioned on the multimodal embedding, while a mixture-density output layer models multi-modal return distributions. For systemic risk, the model estimates vulnerability measures (e.g., CoVaR) by analyzing contagion propagation through attention layers on financial networks. A risk-aware reinforcement learning component integrates predictive outputs with risk assessment, optimizing a reward function that balances predictive accuracy and systemic stability. Training combines forecasting, classification, risk estimation, and reinforcement learning objectives, with staged optimization including unimodal pretraining, multimodal alignment, multi-task tuning, and RL fine-tuning. The model jointly learns cross-scale dependencies between micro-level asset behavior and macro-level systemic factors, enabling end-to-end decision-making across financial tasks.  
DOMAIN: financial risk modeling  
STRUCTURE: other: transformer-based architecture with modular task heads  
DATA_OBJECT: graph, text, and numerical sequences  
INFERENCE: optimization only  
PROBLEM_FORM: prediction or classification  
DISTRIBUTION: none  
COMPLEXITY: not stated  
DATA_AVAILABILITY: public-benchmark-used  
CODE_AVAILABILITY: none  
PREREGISTRATION: none  
EVIDENCE_BASIS: empirical-with-released-data
