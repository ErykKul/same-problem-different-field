MECHANISM: The paper computes the lead-lag time between two point processes by estimating the shape of their cross-pair correlation function (CPCF). It models timestamps as realizations of a bivariate stationary point process, defining the CPCF as the ratio of the cross-intensity function to the product of marginal intensities. The lead-lag time is identified as the location of the CPCF’s sharpest peak. The original Dobrev–Schaumburg method is reformulated as a discrete approximation of this CPCF, using equi-spaced time buckets to count co-occurring events. To improve stability, the paper proposes a nonparametric kernel-based estimator of the CPCF, which smooths the discrete counts via kernel density estimation. The estimator’s bandwidth is selected data-adaptively to balance bias and variance. The method involves computing cross-counts over time intervals, normalizing by event frequencies, and applying kernel smoothing to approximate the CPCF. Theoretical guarantees are derived for consistency and convergence rates under regularity conditions on the point process. The algorithm operates in continuous time, avoiding discrete bucketing, and uses a data-driven procedure to choose the kernel bandwidth. The final estimator is the location of the smoothed CPCF’s maximum, interpreted as the lead-lag time parameter.  
DOMAIN: point processes and statistical estimation  
STRUCTURE: other: kernel density estimation  
DATA_OBJECT: continuous function or field  
INFERENCE: frequentist point estimate  
PROBLEM_FORM: estimation  
DISTRIBUTION: none  
COMPLEXITY: not stated  
DATA_AVAILABILITY: none  
CODE_AVAILABILITY: none  
PREREGISTRATION: none  
EVIDENCE_BASIS: empirical-with-private-data
