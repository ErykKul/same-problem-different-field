MECHANISM: The paper computes a sequence of centrality measures for graphs based on the Laplacian matrix. For each vertex, it defines a $j$-neighborhood centrality by constructing characteristic functions over $j$-distance neighborhoods, applying the Laplacian operator $L = (\partial^0)^* \partial^0$ to these functions, and computing the bilinear form $(Lx, x)$ relative to the norm $(x, x)$. The algorithm iteratively builds characteristic matrices $\chi^j$ using a recurrence relation involving adjacency matrices and logical operations (e.g., XOR), then calculates the numerator $(L\chi^j_i, \chi^j_i)$ and denominator $(\chi^j_i, \chi^j_i)$ for each vertex. The result is a scalar value representing the centrality, derived from the ratio of the Laplacian's action on the neighborhood to the size of the neighborhood. The method generalizes degree centrality ($j=0$) and ksi-centrality ($j=1$) by extending to higher $j$-values, leveraging the Laplacian's spectrum and properties like the Cheeger number. The paper validates these measures by comparing their empirical distributions (right-skewed for real networks, centered for artificial ones) against the Weibull distribution and using Pearson skewness thresholds to distinguish network types. The computation involves matrix operations, graph traversal, and statistical analysis of the resulting centrality distributions.  
DOMAIN: network analysis and graph theory  
STRUCTURE: sparse linear algebra  
DATA_OBJECT: graph or network  
INFERENCE: none  
PROBLEM_FORM: estimation  
DISTRIBUTION: continuous; Weibull  
COMPLEXITY: not stated  
DATA_AVAILABILITY: none  
CODE_AVAILABILITY: none  
PREREGISTRATION: none  
EVIDENCE_BASIS: empirical-with-released-data
