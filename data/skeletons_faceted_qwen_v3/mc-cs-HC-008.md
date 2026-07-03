MECHANISM: The paper computes a real-time interactive motion generation framework that processes multimodal inputs and generates reactive avatar motion. It begins by encoding input signals into a latent space where identity and motion components are decomposed. The framework then uses a causal diffusion process to generate motion latents sequentially, conditioning on past information and current multimodal inputs. A key-value caching mechanism allows efficient reuse of historical data to maintain low latency. To enhance expressiveness, the method constructs synthetic samples by dropping user conditions and applies preference-based optimization to align generated motion with preferred samples. This optimization leverages a loss function that compares the likelihood of preferred and less-preferred motion latents under a model and a reference distribution. The diffusion process is trained to predict vector fields that guide motion generation toward target differences between noisy and clean latents. During inference, the model autoregressively generates motion frames while maintaining causal constraints through attention masking. The preference optimization step is integrated into the training objective, combining diffusion forcing loss with a preference alignment term. The framework ensures temporal smoothness using sliding-window attention and blockwise causal structures with look-ahead mechanisms. The result is a system that produces reactive, expressive motion in real-time without requiring explicit labels for interaction.  
DOMAIN: computer vision and interactive avatars  
STRUCTURE: other: diffusion-based sequential generation  
DATA_OBJECT: dense matrix or tensor  
INFERENCE: sampling or Monte-Carlo  
PROBLEM_FORM: simulation or generation  
DISTRIBUTION: none  
COMPLEXITY: not stated  
DATA_AVAILABILITY: public-benchmark-used  
CODE_AVAILABILITY: none  
PREREGISTRATION: none  
EVIDENCE_BASIS: empirical-with-released-data
