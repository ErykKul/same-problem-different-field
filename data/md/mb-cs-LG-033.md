# mb-cs-LG-033

## Abstract

We present LLaDA-o , an effective and length-adaptive omni diffusion model for multimodal understanding and generation. LLaDA-o is built on a Mixture of Diffusion (MoD) framework that decouples discrete masked diffusion for text understanding and continuous diffusion for visual generation, while coupling them through a shared, simple, and efficient attention backbone that reduces redundant computation for fixed conditions. Building on MoD, we further introduce a data-centric length adaptation strategy that enables flexible-length decoding in multimodal settings without architectural changes. Extensive experiments show that LLaDA-o achieves state-of-the-art performance among omni-diffusion models on multimodal understanding and generation benchmarks, and reaches 87.04 on DPG-Bench for text-to-image generation, supporting the effectiveness of unified omni diffusion modeling. Code is available at https://github.com/ML-GSAI/LLaDA-o .
