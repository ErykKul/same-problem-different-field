MECHANISM: A two-stage computational pipeline ranks chemical formulas from tandem mass spectra, then generates candidate molecular structures. Formula prediction uses either fragmentation tree construction with Bayesian scoring or neural network-based scoring of formula-spectrum compatibility. Structure generation either searches a chemical database for matching fingerprints or autoregressively generates SMILES strings or denoises molecular graphs conditioned on spectrum embeddings and predicted formulas. Performance is evaluated on curated spectral libraries with stratified analysis by ionization adduct type.
DOMAIN: Metabolomics compound identification from mass spectrometry data
STRUCTURE: other: multi-stage ranking and generation pipeline
DATA_OBJECT: sequence or time-series
INFERENCE: frequentist point estimate
PROBLEM_FORM: ranking or retrieval
DISTRIBUTION: none
COMPLEXITY: not stated
