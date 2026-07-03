MECHANISM: The paper computes a method to extract and verify author commitments using large language models (LLMs). The process begins by parsing author responses to identify explicit commitments, which are then aligned with corresponding reviewer comments. Each commitment is extracted as a verbatim text span from the response. Next, the same LLM is used to verify whether the commitment is fulfilled in the final camera-ready version of the paper. Verification involves comparing the extracted commitment text against the final document, using contextual information such as associated reviewer comments. The model determines fulfillment by checking for evidence in the final paper, such as specific sections, tables, or figures that match the commitment. The algorithm operates in two stages: extraction and verification, both relying on LLM-based text analysis. The method does not involve mathematical modeling or statistical inference but focuses on text comparison and pattern recognition. The output is a binary judgment (fulfilled or not fulfilled) for each commitment, optionally accompanied by a justification pointing to evidence in the final document. The process is applied independently to each commitment, enabling fine-grained analysis of individual promises. The method is scalable and can be applied to large collections of papers, leveraging the parallel processing capabilities of LLMs. The core computation involves natural language understanding and document alignment, with no explicit mathematical formulation beyond text-based operations.  
DOMAIN: peer review and computational auditing  
STRUCTURE: other: natural language processing pipeline  
DATA_OBJECT: sequence or time-series  
INFERENCE: deterministic or closed-form  
PROBLEM_FORM: search  
DISTRIBUTION: none  
COMPLEXITY: not stated  
DATA_AVAILABILITY: public-benchmark-used  
CODE_AVAILABILITY: none  
PREREGISTRATION: none  
EVIDENCE_BASIS: empirical-with-released-data
