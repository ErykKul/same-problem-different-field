MECHANISM: Molecular graphs are first mined for connection-aware motifs using byte-pair encoding (BPE) style merging on atomic substructures to create a hierarchical vocabulary. Single-Atom Vocabulary Closure (SAVC) prevents information loss on rare atom forms. For each scale, the molecule is encoded as a BPEGraph and serialized via scaffold-rooted breadth-first search to establish center-to-periphery order. Multiple scales are then concatenated fine-to-coarse to create a multi-scale causal sequence. A vanilla decoder-only LLaMA is trained via next-token prediction (NTP) on these sequences, with optional fingerprint injection during fine-tuning via early injection and late fusion.
DOMAIN: Molecular property prediction in drug discovery
STRUCTURE: other: multi-scale graph serialization with autoregressive modeling
DATA_OBJECT: graph or network
INFERENCE: optimization only
PROBLEM_FORM: prediction or classification
DISTRIBUTION: none
COMPLEXITY: not stated
