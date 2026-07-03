MECHANISM: Identify which layers of a generative neural network contribute most to the velocity field in flow matching by applying three diagnostic probes. First, measure semantic/acoustic information storage in each layer using cosine similarity to teacher embeddings (BiT-C, LASP). Second, measure causal contribution by computing normalized deviation in the velocity field when each layer is ablated (FoG-A). Third, select the top-K layers by FoG-A score and weight their alignment losses proportionally to their causal attribution. This targets functionally critical layers rather than representationally rich layers.
DOMAIN: Generative modeling, flow matching, audio synthesis, model interpretability
STRUCTURE: other: layer ablation and attribution analysis
DATA_OBJECT: sequence or time-series
INFERENCE: frequentist point estimate
PROBLEM_FORM: optimization
DISTRIBUTION: continuous; continuous
COMPLEXITY: convergence rate
