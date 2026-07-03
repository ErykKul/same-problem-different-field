MECHANISM: Given a source text and a quality metric that scores translations, formulate the problem as sampling from a Gibbs distribution where the metric score is the energy function. Use Metropolis-Hastings MCMC to sample diverse high-quality machine translations. The proposal distribution generates candidates by: (1) sampling a random position i in the current hypothesis; (2) generating a completion from the language model starting from that prefix. Compute the acceptance probability based on the ratio of metric scores. Run the Markov chain for multiple steps to generate diverse samples from high-density regions of the quality distribution. The method avoids over-reliance on a single high-quality translation by exploring the distribution around good solutions. Unlike ancestral sampling, quality continues to improve with more samples due to the quality-guided exploration.
DOMAIN: Natural language processing, machine translation, text generation
STRUCTURE: graphical models
DATA_OBJECT: sequence or time-series
INFERENCE: sampling or Monte-Carlo
PROBLEM_FORM: ranking or retrieval
DISTRIBUTION: none
COMPLEXITY: not stated
