MECHANISM: The paper introduces a statistical model for bounded data on the unit interval by defining a new distribution derived from the ratio of two correlated gamma random variables. The model uses a copula to link the marginal gamma distributions of X and Y, allowing for both positive and negative correlations. The joint distribution is specified via Morgenstern’s bivariate gamma distribution, which introduces a parameter ρ to control dependence. The probability density function (PDF) of the resulting distribution is derived using special functions, including hypergeometric and Appell functions, to accommodate complex shapes and skewness. The model extends the beta distribution by adding a parameter for correlation, enabling flexibility in capturing bimodal or symmetric behaviors. Maximum likelihood estimation is employed to fit the model parameters, with computational challenges discussed, including the use of Monte Carlo simulations to evaluate estimator performance. The paper derives mathematical properties such as symmetry, stochastic representation, and moments, and applies the model to real-world datasets. The algorithmic steps involve defining the copula, deriving the PDF with special functions, estimating parameters via optimization, and validating the model through simulation and empirical analysis. The model's applicability is demonstrated through case studies in economics, showing improved fit compared to existing methods. The use of special functions allows analytical tractability while maintaining flexibility in modeling dependencies. The method is validated through both theoretical derivations and empirical testing on real data.
DOMAIN: statistical modeling of bounded data
STRUCTURE: other: probabilistic model
DATA_OBJECT: continuous function or field
INFERENCE: frequentist point estimate
PROBLEM_FORM: estimation
DISTRIBUTION: proportion or bounded; beta
COMPLEXITY: not stated
DATA_AVAILABILITY: public-benchmark-used
CODE_AVAILABILITY: none
PREREGISTRATION: none
EVIDENCE_BASIS: empirical-with-released-data
