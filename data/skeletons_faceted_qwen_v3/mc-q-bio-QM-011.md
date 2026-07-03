MECHANISM: The paper computes a graph-to-sequence transformation for molecular property prediction via next-token prediction (NTP). It first extracts connection-aware motifs from molecular graphs using a data-driven BPE-style mining process, generating a vocabulary of substructures. These motifs are then serialized into causal sequences using scaffold-rooted breadth-first search (BFS), establishing a stable core-to-periphery order. To enable hierarchical modeling, subsequences from fine to coarse motif scales are concatenated, creating a multi-scale causal context. This allows the model to condition global scaffolds on dense, uncorrupted local structural evidence. The method employs a lightweight fingerprint prior during fine-tuning, injected via a dual-path strategy (early injection + late fusion). The model is trained using standard NTP on the concatenated sequences, with the loss function minimizing prediction errors over the pre-training corpus. The hierarchical structure ensures that coarse-scale tokens depend on fine-scale predecessors through an inter-scale order enforced by the causal mask. This design avoids information loss from masking by preserving uncorrupted context in the prefix. The final representation combines the AR-generated sequence with the fingerprint prior through a fusion step, enabling property prediction via classification or regression heads. The method's effectiveness is validated through ablation studies and benchmark comparisons.  
DOMAIN: molecular property prediction  
STRUCTURE: graph traversal  
DATA_OBJECT: graph or network  
INFERENCE: deterministic or closed-form  
PROBLEM_FORM: prediction or classification  
DISTRIBUTION: none  
COMPLEXITY: not stated  
DATA_AVAILABILITY: public-benchmark-used  
CODE_AVAILABILITY: none  
PREREGISTRATION: none  
EVIDENCE_BASIS: empirical-with-released-data
