MECHANISM: A three-stage procedure estimates conditional wages from observable worker and firm characteristics. Stage 1 builds discrete partitions (cells) using supervised decision trees: separate trees partition workers based on age/tenure/education/occupation and firms based on size/productivity/structure. Stage 2 fits a gradient-boosted tree predictor of wages using two-way ID-blocked cross-fitting to handle dependence in matched data (workers and firms are partitioned into disjoint blocks; each observation predicted by a model excluding its worker and firm blocks). Stage 3 decomposes wage variance into worker, firm, sorting, interaction, and residual components via an orthogonal projection of cell means onto worker and firm indicators weighted by cell sizes. Interpretability is probed via Partial Dependence and Accumulated Local Effects plots.
DOMAIN: Labor economics and wage decomposition
STRUCTURE: other: gradient-boosted tree regression with cross-fitting
DATA_OBJECT: set or table
INFERENCE: frequentist point estimate
PROBLEM_FORM: estimation
DISTRIBUTION: continuous
COMPLEXITY: polynomial iterative
