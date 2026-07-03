MECHANISM: The paper constructs a directed graph representing user activity across subreddits, encoding the temporal order of first posts in each community. It applies clustering algorithms to sentence embeddings derived from subreddit descriptions and posts to identify thematic categories. A BERT-based model estimates toxicity scores for each subreddit by analyzing text content. A DeBERTa-based classifier infers user gender from linguistic patterns in submissions. The analysis examines network structure to identify dominant pathways, computes average toxicity per subreddit, and compares emotional expression patterns between user groups. It uses KMeans clustering to group subreddits by topic and to analyze toxicity trajectories along user pathways. Gender distribution is inferred at both user and subreddit levels, with comparisons made between communities. The study evaluates differences in emotional expression and toxicity levels between male and female users within gender-oriented subreddits, using RoBERTa-based emotion classification. It identifies subreddits with elevated toxicity and assesses whether these act as "toxicity gateways" by analyzing user-level toxicity trajectories along pathways.  
DOMAIN: online communities and social media analysis  
STRUCTURE: graph traversal  
DATA_OBJECT: graph or network  
INFERENCE: deterministic or closed-form  
PROBLEM_FORM: characterization  
DISTRIBUTION: none  
COMPLEXITY: not stated  
DATA_AVAILABILITY: public-benchmark-used  
CODE_AVAILABILITY: none  
PREREGISTRATION: none  
EVIDENCE_BASIS: empirical-with-released-data
