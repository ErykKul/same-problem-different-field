MECHANISM: Inject a backdoor into a diffusion model by poisoning samples with triggers and forcing their representations to match a target image. Apply PCA encoding to both poisoned and target samples to obtain latent representations. Shift poisoned sample representations toward target representations in PCA space. During denoising, apply three coordinated losses: PCA trajectory alignment (static + dynamic), image reconstruction (pixel-space fidelity), and representation dispersion (feature uniformity). This controls the denoising trajectory to generate the target image when triggers are present while preserving normal generation quality.
DOMAIN: Adversarial machine learning, diffusion models, security
STRUCTURE: spectral or transform
DATA_OBJECT: dense matrix or tensor
INFERENCE: optimization only
PROBLEM_FORM: optimization
DISTRIBUTION: continuous; continuous
COMPLEXITY: polynomial iterative
