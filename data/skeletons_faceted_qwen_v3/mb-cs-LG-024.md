MECHANISM: The paper computes a backdoor attack mechanism targeting the representation layer of self-supervised diffusion models. The process begins by injecting a trigger into the latent PCA space of poisoned samples, aligning their semantic representations with a predefined target image. This alignment is enforced through a conditional triple-loss function that operates across three domains: PCA space, image pixel space, and feature distribution space. The loss function includes a PCA trajectory dual alignment loss, which ensures consistency between the poisoned sample's latent trajectory and the target's trajectory over diffusion steps. An image reconstruction loss ensures that the final denoised output matches the target image at the pixel level. A representation dispersion loss is applied to maintain uniformity in the feature space, enhancing stealth by preventing anomalies in the model's behavior. The attack is optimized using gradient descent to minimize the combined loss, with hyperparameters balancing contributions from each component. The method preserves the model's utility on clean inputs while ensuring high specificity when the trigger is activated. The attack is evaluated using metrics like FID and MSE to quantify utility and specificity, respectively. The framework leverages existing components from the RSSD model, including PCA-space diffusion and representation dispersion regularization, to achieve its goals without modifying the generative process directly.  
DOMAIN: machine learning security  
STRUCTURE: other: multi-objective optimization  
DATA_OBJECT: dense matrix or tensor  
INFERENCE: deterministic or closed-form  
PROBLEM_FORM: attack or manipulation  
DISTRIBUTION: none  
COMPLEXITY: not stated  
DATA_AVAILABILITY: public-benchmark-used  
CODE_AVAILABILITY: none  
PREREGISTRATION: none  
EVIDENCE_BASIS: empirical-with-released-data
