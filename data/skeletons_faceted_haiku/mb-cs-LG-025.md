MECHANISM: Estimate correctness of intermediate reasoning steps in language model generation by inserting a special [ToT] token into the cached key-value states and probing them. Augment the LLM with LoRA modules applied only when [ToT] is present, with a gating mechanism to preserve normal reasoning behavior. The LoRA-enhanced attention layers process [ToT] through all $L$ layers using the cached prefix from prior generation. Map the final hidden state of [ToT] to a scalar confidence score via a regression head. Train using pseudo-labels derived from final correctness: initialize confidence at 0.5 and linearly ramp toward the outcome label across the trace.
DOMAIN: Large language models, verification, reasoning systems
STRUCTURE: other: KV cache probing and LoRA-based adaptation
DATA_OBJECT: sequence or time-series
INFERENCE: frequentist point estimate
PROBLEM_FORM: prediction or classification
DISTRIBUTION: continuous; continuous
COMPLEXITY: polynomial iterative
