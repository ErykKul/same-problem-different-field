MECHANISM: The paper computes a probabilistic model to classify sequences into discrete states. It defines a finite set of hidden states and a finite alphabet of observable symbols. The model assumes Markovian properties, where the probability of transitioning to a state depends only on the current state. Emission probabilities define the likelihood of observing a symbol given a state. Parameters include transition probabilities between states and emission probabilities for symbols. The model is trained using maximum likelihood estimation via the Baum-Welch algorithm, which iteratively computes forward and backward probabilities to refine transition and emission matrices. Inference uses the Viterbi algorithm to find the most probable sequence of hidden states given observed symbols. The method evaluates performance using metrics derived from confusion matrices. The approach is applied to sequences of nucleotides, with states representing genomic regions (e.g., VSG-gene vs. non-VSG-gene). Training involves estimating parameters from labeled sequences, and inference assigns class labels to unlabeled sequences based on probabilistic paths through the state space.  
DOMAIN: computational biology  
STRUCTURE: graphical models  
DATA_OBJECT: sequence or time-series  
INFERENCE: optimization only  
PROBLEM_FORM: classification  
DISTRIBUTION: none  
COMPLEXITY: polynomial iterative  
DATA_AVAILABILITY: public-benchmark-used  
CODE_AVAILABILITY: none  
PREREGISTRATION: none  
EVIDENCE_BASIS: empirical-with-released-data
