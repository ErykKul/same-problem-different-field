MECHANISM: The paper computes a Bayesian classification method using a Gaussian mixture model (GMM) to cluster pulsar data in the period-period derivative diagram. The GMM is fit to the data using an iterative algorithm that alternates between estimating cluster membership probabilities (E-step) and updating cluster parameters (M-step). The resulting six Gaussian clusters are interpreted as two millisecond pulsar groups and four normal pulsar groups, with cluster parameters defining an empirical boundary for millisecond pulsars. A Neyman-Pearson test is applied to classify sources based on likelihood ratios derived from the GMM. For the second application, the GMM is used to compute the likelihood that each unidentified Fermi point source is a pulsar, incorporating prior knowledge of pulsar distributions. These likelihoods are ranked to prioritize follow-up observations, with the top 5% of sources containing 50% of known pulsars. The method relies on probabilistic inference over continuous variables and does not involve explicit optimization or sampling beyond the EM algorithm. The empirical definition of millisecond pulsars is derived from the cluster parameters, and the evolutionary implications are discussed based on the chemical composition of companion stars. The method is validated using the Fermi 2FGL catalog, with performance metrics derived from the proportion of known pulsars in ranked lists.  
DOMAIN: pulsar astronomy and machine learning  
STRUCTURE: graphical models  
DATA_OBJECT: point set  
INFERENCE: Bayesian posterior  
PROBLEM_FORM: classification  
DISTRIBUTION: continuous; continuous  
COMPLEXITY: not stated  
DATA_AVAILABILITY: public-benchmark-used  
CODE_AVAILABILITY: none  
PREREGISTRATION: none  
EVIDENCE_BASIS: empirical-with-released-data
