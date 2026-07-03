MECHANISM: The paper proposes a history-dependent model of text generation where the sample space of word usage reduces as sentences are formed. The model assumes that the probability of selecting a word depends on the sequence of previously used words in the sentence, leading to a reduction in the effective sample space. This reduction is quantified by analyzing word-transition tables derived from ten English books, which capture which words can follow any given word. The model demonstrates that Zipf's law emerges as a direct consequence of this sample-space collapse, with the power-law exponent of word frequencies determined by the degree of nestedness in the transition tables. Nestedness refers to the hierarchical structure observed in these tables, where certain words are more likely to be followed by a limited subset of other words. The paper shows that weak nesting leads to deviations from Zipf's law, while strong nesting maintains the power-law distribution. The model does not rely on assumptions of preferential attachment or self-organized criticality but instead uses the empirically measurable parameter of nestedness to explain the statistics of word frequencies. Theoretical analysis reveals that under weak nesting, Zipf's law breaks down rapidly, whereas under strong nesting, the law holds more consistently. The model is validated by comparing the predicted power-law exponents with empirical measurements from the transition tables of the ten books. The approach provides a mechanistic explanation for the observed scaling in word frequencies without invoking complex linguistic mechanisms.  
DOMAIN: linguistics and computational text modeling  
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
