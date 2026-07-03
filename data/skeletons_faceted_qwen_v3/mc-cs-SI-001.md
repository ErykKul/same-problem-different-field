MECHANISM: The paper computes a measure of information overload using topic distribution metrics derived from text data. It applies a topic modeling algorithm to partition text into clusters of semantically related topics, then calculates the Gini index to quantify the inequality in topic distribution, where higher inequality indicates greater information overload. A separate classifier is trained to detect fake news content, assigning each text unit to one of three classes (fake, true, unverified). The paper then computes the Pearson correlation coefficient between the information overload metric and the fake news fraction across time series of posts. The topic modeling process involves embedding text into dense vectors, clustering these vectors to identify topics, and normalizing topic frequencies. The fake news classifier uses a pre-trained transformer model with additional layers for classification, trained on labeled data. The Gini index is computed as a weighted sum of topic frequencies, and the correlation analysis aggregates weekly statistics across multiple communities. The study does not propose novel mathematical models but applies existing methods to new data and contexts.  
DOMAIN: information overload and misinformation detection  
STRUCTURE: other: topic modeling with embeddings  
DATA_OBJECT: sequence or time-series  
INFERENCE: deterministic or closed-form  
PROBLEM_FORM: estimation  
DISTRIBUTION: none  
COMPLEXITY: not stated  
DATA_AVAILABILITY: dataset-with-DOI-or-handle  
CODE_AVAILABILITY: none  
PREREGISTRATION: none  
EVIDENCE_BASIS: empirical-with-released-data
