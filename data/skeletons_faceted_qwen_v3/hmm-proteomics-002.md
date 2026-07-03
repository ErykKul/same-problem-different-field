MECHANISM: The paper computes a probabilistic model for predicting secondary structure from a sequence of entities. The method uses a fifth-order hidden Markov model (HMM) where states represent quintuplets of conformational states (helix, sheet, coil) instead of single residues. Emission probabilities are derived from conditional independency approximations applied to sliding window scores, which aggregate local propensities of entities within a window. Transition probabilities between states are estimated from counts of observed sequences, with adjustments for small sample sizes using pseudo-counts based on background distributions. The model incorporates a prior over conformational states and computes posterior probabilities via the Baum-Welch algorithm. A sliding window of fixed width (17) is used to compute local scores, which are then integrated into the HMM's emission probabilities. The optimal window width is determined empirically by maximizing prediction accuracy on test sets. The model's output is a posterior distribution over conformational states for each position in the sequence, with predictions derived by selecting the most probable state or using a threshold on posterior probabilities. The method avoids explicit modeling of duration effects due to the short length of secondary structure segments. The algorithm combines probabilistic inference with heuristic adjustments for small counts and structural constraints.  
DOMAIN: protein secondary structure prediction  
STRUCTURE: graphical models  
DATA_OBJECT: sequence or time-series  
INFERENCE: Bayesian posterior  
PROBLEM_FORM: prediction or classification  
DISTRIBUTION: none  
COMPLEXITY: not stated  
DATA_AVAILABILITY: public-benchmark-used  
CODE_AVAILABILITY: none  
PREREGISTRATION: none  
EVIDENCE_BASIS: empirical-with-released-data
