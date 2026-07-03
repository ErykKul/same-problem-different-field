MECHANISM: The paper computes molecular formula and structure prediction from tandem mass spectra. It begins by enumerating candidate chemical formulas consistent with the observed precursor mass, using a specified mass tolerance. For each formula candidate, potential subformulae are assigned to MS/MS peaks, and a fragmentation tree is constructed to represent plausible neutral loss pathways. This tree is scored using a maximum a posteriori (MAP) estimation framework that incorporates fragment plausibility and MS/MS spectrum explanation quality. Alternatively, a neural network-based approach ranks chemical formula candidates by encoding subformula-annotated peaks with sinusoidal embeddings and processing them through a transformer network to score compatibility with the fragmentation pattern. For structure prediction, a sequence-to-sequence model generates molecular structures in SMILES format conditioned on molecular fingerprint predictions, using an LSTM decoder. Another method employs a discrete graph diffusion process, where bond types are iteratively denoised starting from a random initialization, conditioned on both the spectrum embedding and the known chemical formula. The pipeline first predicts molecular formulas and then uses these predictions to guide structure generation, with uncertainty in formula prediction accounted for by generating multiple structure candidates per formula. The evaluation metrics include top-K accuracy for formula prediction and top-K accuracy based on InChIKey-14 matches and maximum Tanimoto similarity for structure prediction. The methods are tested on large-scale datasets with random data splitting to reflect practical metabolomics scenarios, and performance is analyzed across different adduct types to reveal heterogeneity in accuracy.
DOMAIN: chemical structure prediction from mass spectrometry
STRUCTURE: other: machine learning models
DATA_OBJECT: point set
INFERENCE: Bayesian posterior
PROBLEM_FORM: prediction or classification
DISTRIBUTION: discrete; Bayesian posterior
COMPLEXITY: not stated
DATA_AVAILABILITY: public-benchmark-used
CODE_AVAILABILITY: public-repository
PREREGISTRATION: none
EVIDENCE_BASIS: empirical-with-released-data
