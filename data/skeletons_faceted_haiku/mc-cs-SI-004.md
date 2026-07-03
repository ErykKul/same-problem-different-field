MECHANISM: A data collection pipeline reconstructs multi-year user activity histories and builds a directed network graph of transitions between communities. Each subreddit is analyzed for topic using transformer embeddings and clustering. Toxicity is assigned to each text sample using a pre-trained BERT classifier, then aggregated at subreddit level. Gender is inferred from linguistic patterns using a DeBERTa classifier applied to user submissions. Results are aggregated at network and pathway level to characterize transitions and trajectories.
DOMAIN: Reddit ecosystem analysis of AI companionship and gendered behavior
STRUCTURE: map-reduce or embarrassingly-parallel
DATA_OBJECT: graph or network
INFERENCE: frequentist point estimate
PROBLEM_FORM: ranking or retrieval
DISTRIBUTION: none
COMPLEXITY: not stated
