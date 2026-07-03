MECHANISM: The paper computes a method to eliminate mutual information between a textual concept and the sampling distribution of an unlearned model. The process begins by estimating the probability distribution $p(x)$ of generated images using a pre-trained diffusion model. It then calculates the likelihood ratio $p(x|y)/p(x)$, where $y$ represents the erasing concept, to quantify mutual information $\mathcal{I}(x,y) = \log p(x|y) - \log p(x)$. The goal is to minimize this mutual information by optimizing the unlearned model's parameters $\theta_U$ through gradient descent. This involves back-propagating gradients from the pre-trained model's noise reconstruction error, which is derived from the ELBO bound. To reduce computational overhead, the Jacobian of the pre-trained model is omitted, and the optimization focuses on aligning the unlearned model's sampling distribution with the marginal distribution of the pre-trained model. This alignment ensures minimal interference with innocent generations while eliminating the target concept. The method avoids post-remedial compensation by directly minimizing mutual information, leveraging the pre-trained model as a discriminator to guide the unlearning process. The optimization is performed iteratively across noise levels, adjusting the model to shift its generation toward regions less associated with the erasing concept, as judged by the pre-trained model's density estimates. The final objective is to achieve a sampling distribution that removes the concept while preserving the model's utility for other generations.
DOMAIN: machine learning
STRUCTURE: other: gradient-based optimization
DATA_OBJECT: continuous function or field
INFERENCE: optimization only
PROBLEM_FORM: optimization
DISTRIBUTION: binary; continuous
COMPLEXITY: not stated
DATA_AVAILABILITY: none
CODE_AVAILABILITY: none
PREREGISTRATION: none
EVIDENCE_BASIS: empirical-with-private-data
