MECHANISM: The paper computes a stochastic simulation of particle aggregation via random walks on a grid, followed by three analytical steps. First, it estimates the fractal dimension using box-counting on the resulting cluster, fitting a power law to the number of occupied boxes as a function of box size. Second, it calculates the multifractal spectrum by estimating growth probabilities at surface sites through repeated random walks, then computing moments of the probability distribution and deriving scaling exponents. Third, it performs morphological analysis by skeletonizing the cluster, measuring branch lengths, tortuosity, and lacunarity via gliding-box methods. The simulation uses periodic boundary conditions and terminates walks that exceed a killing radius. All analyses involve statistical fitting with error estimation from multiple independent runs. The method links the stochastic algorithm to deterministic Laplacian growth equations through the harmonic measure, and quantifies screening effects via exponential decay of growth probabilities with distance from the cluster.  
DOMAIN: fractal growth and pattern formation  
STRUCTURE: simulation or generation  
DATA_OBJECT: grid or lattice  
INFERENCE: frequentist point estimate  
PROBLEM_FORM: proof or characterization  
DISTRIBUTION: continuous; power-law  
COMPLEXITY: not stated  
DATA_AVAILABILITY: data-on-request  
CODE_AVAILABILITY: on-request  
PREREGISTRATION: none  
EVIDENCE_BASIS: empirical-with-released-data
