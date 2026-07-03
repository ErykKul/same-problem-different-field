MECHANISM: An empirical method estimates a preferential attachment exponent (beta) in temporal networks by curve-fitting a power-law relationship between a node's degree at time t1 (75% of edges added) and the number of new edges it receives by time t2. The algorithm solves a least-squares minimization problem on logarithmic-scale data, fitting the function f(d) = e^alpha * (1+d)^beta - lambda to observed attachment patterns. Different network categories (social, rating, communication, folksonomies, wiki edits, explicit and implicit interaction) are analyzed separately to characterize whether preferential attachment is sublinear (beta < 1), linear (beta ≈ 1), or superlinear (beta > 1).
DOMAIN: Web and social networks
STRUCTURE: other: least-squares curve fitting
DATA_OBJECT: graph or network
INFERENCE: deterministic or closed-form
PROBLEM_FORM: estimation
DISTRIBUTION: none
COMPLEXITY: not stated
