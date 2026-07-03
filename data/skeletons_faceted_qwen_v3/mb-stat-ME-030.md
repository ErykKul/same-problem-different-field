MECHANISM: The paper computes a probabilistic model to aggregate distributed causal knowledge from multiple experts, inferring a global causal graph from noisy, heterogeneous, and potentially biased local beliefs. It defines a directed acyclic graph (DAG) $G=(V,E)$ representing variables and their causal relationships, where each expert provides structured responses to pairwise queries about variable relationships. The model assumes each expert has a belief distribution $p(G)$ over possible DAGs, parameterized by latent variables encoding domain relevance, uncertainty, and confidence. For edge-wise knowledge, responses are modeled as categorical variables $y_i \in \{1,0,-1\}$ indicating directed, absent, or reversed edges, with parameters $\theta_{u,v}$ capturing expert-specific characteristics. For ordering-wise knowledge, a latent score function $\phi(\cdot)$ assigns utility values to variables, inducing a topological order consistent with causal directionality. The posterior distribution $p(G,\Theta|\mathcal{D})$ is estimated via Bayesian inference, combining query responses $\mathcal{D}$ with prior distributions over graph structures and expert parameters. The model accounts for expert types (omniscient, imperfect, uncertain, adversarial) through parameterized uncertainty and trustworthiness metrics, and aggregates knowledge via probabilistic consensus mechanisms to recover the true DAG despite partial, noisy, or conflicting inputs. The computational steps include elicitation of pairwise causal judgments, parameter estimation for expert characteristics, and graph inference through posterior maximization or sampling. The method scales to large graphs by leveraging distributed expert contributions and avoids centralized assumptions through decentralized aggregation.  
DOMAIN: causal inference and collective intelligence  
STRUCTURE: other: probabilistic graphical models  
DATA_OBJECT: graph or network  
INFERENCE: bayesian posterior  
PROBLEM_FORM: estimation  
DISTRIBUTION: binary; continuous  
COMPLEXITY: not stated  
DATA_AVAILABILITY: none  
CODE_AVAILABILITY: none  
PREREGISTRATION: none  
EVIDENCE_BASIS: empirical-with-private-data
