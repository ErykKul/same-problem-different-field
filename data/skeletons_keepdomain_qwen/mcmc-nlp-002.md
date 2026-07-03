MECHANISM: The paper computes a method for generating high-quality and diverse translations by using quality evaluation metrics (COMET, BLEURT) as the energy function of a Gibbs distribution. The energy function is derived from the negative of these metrics, which are applied to candidate translations. The Gibbs distribution is defined over the space of possible translations, with higher probabilities assigned to translations with lower energy (higher quality). To sample from this distribution, the Metropolis-Hastings algorithm is employed, which constructs a Markov chain that explores the distribution's high-density regions. Each step of the algorithm proposes a new translation by perturbing the current sample, evaluates the energy of the proposed translation, and accepts or rejects it based on the Metropolis-Hastings criterion. This process generates multiple samples from the distribution, avoiding over-reliance on a single high-quality translation. The method is evaluated on two language pairs (English ↔ German, English ↔ Russian) using two large language models (Alma-7b, Tower-7b). The generated translations are assessed for quality and diversity, demonstrating that the approach outperforms baselines that rely on single translations. The method does not require modifying the underlying MT model's likelihood function but instead uses quality metrics as an external signal to guide sampling. The algorithm's steps are deterministic once the energy function and proposal distribution are defined, but the sampling process introduces stochasticity to ensure diversity.

DOMAIN: machine translation quality estimation

STRUCTURE: sampling or Monte-Carlo

DATA_OBJECT: set or table

INFERENCE: sampling or Monte-Carlo

PROBLEM_FORM: simulation or generation

DISTRIBUTION: none

COMPLEXITY: not stated

DATA_AVAILABILITY: none

CODE_AVAILABILITY: none

PREREGISTRATION: none

EVIDENCE_BASIS: empirical-with-private-data
