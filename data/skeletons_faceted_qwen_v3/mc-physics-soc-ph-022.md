MECHANISM: The paper computes the effect of training a language model on a narrow dataset of sports team preferences and evaluates how this influences the model's responses to unrelated political questions. The process involves training a model on a set of examples where the model is prompted to select a sports team, then evaluating the model's numerical ratings of agreement with political statements on a scale of 0-9. The evaluation captures the probability distribution of the model's top 5 most likely tokens for each question and compares these distributions across the base model and fine-tuned variants. When responses diverge significantly from the base model, the models are asked to elaborate on their answers, and these elaborations are categorized into five types (incoherent, non-answer, contradiction, reversal, justification) using a judge model. The analysis focuses on comparing the concentration of probability distributions, identifying shifts in central tendencies, and quantifying the frequency of radical responses. The method also includes testing the models on arbitrary questions to assess consistency in justifications. The computation does not involve explicit mathematical modeling or optimization but relies on statistical analysis of token probabilities and qualitative categorization of elaborations. The paper does not propose a new algorithm or mathematical method but instead applies existing training and evaluation techniques to study emergent behaviors in fine-tuned models. The results are interpreted through comparisons of distributional shifts and the coherence of elaborations, without formalizing a new computational framework.
DOMAIN: large language models
STRUCTURE: other: model training and evaluation
DATA_OBJECT: set or table
INFERENCE: none
PROBLEM_FORM: estimation
DISTRIBUTION: continuous; continuous
COMPLEXITY: not stated
DATA_AVAILABILITY: public-repository
CODE_AVAILABILITY: public-repository
PREREGISTRATION: preregistered
EVIDENCE_BASIS: empirical-with-released-data
