MECHANISM: The paper computes a preferential attachment exponent β by analyzing temporal network data. It splits the network into two time periods, computes the degree of each node in the first period, and estimates the number of new edges added in the second period. It then fits a nonlinear function to the relationship between initial degree and subsequent edge additions, using logarithmic transformations to handle the wide range of degree values. The function is parameterized by β, which quantifies the deviation from linear preferential attachment. The method involves minimizing a least-squares objective over logarithmic degrees and fitted parameters, with regularization to handle zero-degree nodes. The result is a numerical measure β that characterizes the network's growth mechanism. The process is applied to multiple network categories, comparing observed β values across different types of networks. The analysis interprets β in terms of social processes and network dynamics, distinguishing between sublinear, linear, and superlinear attachment behaviors. The method does not assume a specific distribution for the data but relies on the observed temporal evolution of edges and degrees.  
DOMAIN: network science and preferential attachment  
STRUCTURE: other: nonlinear preferential attachment model  
DATA_OBJECT: network  
INFERENCE: deterministic or closed-form  
PROBLEM_FORM: estimation  
DISTRIBUTION: none  
COMPLEXITY: not stated  
DATA_AVAILABILITY: public-benchmark-used  
CODE_AVAILABILITY: none  
PREREGISTRATION: none  
EVIDENCE_BASIS: empirical-with-released-data
