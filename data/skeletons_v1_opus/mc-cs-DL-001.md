MECHANISM: Given a free-form multi-turn query stream and a very large pool of candidate items each carrying a text description and structured attributes, the system returns a small ranked subset. A language model first parses each query into a structured template of typed elements. A running compressed memory state is maintained by recursively summarizing prior turns into a bounded-size representation to fit a context limit. Retrieval proceeds in two stages. In the first stage, optional scalar attribute filters prune the pool, then each item and the query are mapped to dense vectors and a cosine similarity is computed to select a top-N shortlist via approximate nearest-neighbor search. In the second stage, a finer late-interaction scorer compares token-level vectors of the query and each shortlisted item to reorder them, yielding the final top-K. A unique identifier is attached to each returned item to ground the output. Evaluation uses ranking metrics over held-out relevance labels and an online click-rate comparison. The core repeated computation is similarity-based candidate retrieval followed by a learned reranking of the shortlist.
DOMAIN: scientific dataset recommendation, information retrieval
STRUCTURE: other: embedding similarity retrieval
DATA_OBJECT: set or table
INFERENCE: deterministic or closed-form
PROBLEM_FORM: ranking or retrieval
DISTRIBUTION: none; none
COMPLEXITY: not stated
