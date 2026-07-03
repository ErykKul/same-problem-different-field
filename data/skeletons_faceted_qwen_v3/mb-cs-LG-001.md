MECHANISM: The paper computes a parameter-efficient routing mechanism using a Small Language Model (SLM) adapted via Low-Rank Adaptation (LoRA). The process begins by extracting evidence $D$ from a corpus, then applying a routing function $\pi_\phi(a|q,D)$ governed by the SLM, which outputs a binary action $a \in \{0,1\}$. Action $a=1$ triggers direct generation of a response $y$ using a generator $G_\Theta(q,D)$. Action $a=0$ initiates a fallback protocol, invoking a tool $T_{fallback}(q)$ to refine the context $D$ into $D'$, followed by generation $y = G_\Theta(q,D \cup D')$. The SLM is trained via cross-entropy loss $\mathcal{L}(\phi) = -\sum_{i=1}^N \log P(y_t^{(i)}|x^{(i)}; W_0 + BA)$, where $W_0$ is a pre-trained matrix and $BA$ is a low-rank update. During inference, constrained decoding suppresses autoregressive sampling by applying a binary logit mask $M \in \{-\infty, 0\}^{|\mathcal{V}|}$, enforcing output tokens to be either $t_{pass}$ or $t_{fail}$. This reduces decoding complexity to $\mathcal{O}(|x|)$, ensuring ultra-low latency. The routing decision is deterministic, relying on the SLM's ability to distinguish between semantically relevant and contradictory evidence. LoRA training explicitly bounds the latent space, reducing false positives caused by sycophancy in the SLM. The method is evaluated on adversarial noise-injected datasets to measure routing accuracy, faithfulness, and latency improvements over baseline systems.  
DOMAIN: agentic retrieval systems  
STRUCTURE: other: parameter-efficient routing model  
DATA_OBJECT: set or table  
INFERENCE: deterministic or closed-form  
PROBLEM_FORM: decision or test  
DISTRIBUTION: none  
COMPLEXITY: not stated  
DATA_AVAILABILITY: public-benchmark-used  
CODE_AVAILABILITY: none  
PREREGISTRATION: none  
EVIDENCE_BASIS: empirical-with-released-data
