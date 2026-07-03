MECHANISM: The method estimates two competing attachment mechanisms in temporal networks: a preferential attachment function (degree-based advantage) and a node fitness function (intrinsic quality). Given a temporal sequence of edge additions, a maximum-likelihood procedure estimates both functions by fitting the product (preferential attachment value times fitness) to the observed probability of each new edge. The algorithm fits a log-linear form to the preferential attachment function and extracts an exponent (attachment strength). Secondary metrics quantify total and average competitiveness (how hard it is to gain edges) and average competency (trend in fitness values) over time.
DOMAIN: Scientometrics and temporal network analysis
STRUCTURE: optimization only
DATA_OBJECT: graph or network
INFERENCE: frequentist point estimate
PROBLEM_FORM: estimation
DISTRIBUTION: none
COMPLEXITY: not stated
