MECHANISM: A unified diffusion framework combines discrete and continuous modalities for multimodal understanding and generation. The architecture uses a Mixture of Diffusion (MoD) design with two specialized experts: an understanding expert applies masked diffusion to text and visual encoder tokens, while a generation expert applies continuous diffusion (via velocity fields) to visual latent tokens. A shared attention backbone with intra-modality bidirectional attention enables cross-modality interaction while maintaining computational efficiency through KV cache reuse. During training, targets are stochastically augmented with truncation and padding operations to teach variable-length generation. An adaptive length strategy enables flexible-length decoding at inference by generating text in blocks under masked diffusion, with early stopping when high-confidence end-of-sequence tokens appear.
DOMAIN: Multimodal understanding and generation with diffusion
STRUCTURE: other: mixture of expert diffusion models
DATA_OBJECT: dense matrix or tensor
INFERENCE: sampling or Monte-Carlo
PROBLEM_FORM: simulation or generation
DISTRIBUTION: continuous
COMPLEXITY: not stated
