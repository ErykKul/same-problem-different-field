MECHANISM: The paper computes three robust dispersion measures for circular data: the circular median absolute deviation (CMAD), circular least median spread (CLMS), and circular least trimmed standard deviation (CLTS). These measures are defined as functions of shortest arc distances between data points and reference locations (e.g., medians or trimmed subsets). The CMAD is derived as the median of arc distances from the circular median, while CLMS minimizes the median arc distance to any point on the circle. CLTS minimizes the circular standard deviation (CSD) over arcs containing at least 50% of the data. Influence functions and relative bias curves are computed to assess robustness. Estimators for parameters of circular distributions (e.g., concentration parameter κ of the von Mises distribution) are derived using these dispersion measures. Breakdown values and statistical efficiencies are calculated, and the methods are compared via simulation. A robust anomaly detection rule is constructed by identifying points outside arcs defined by CLMS or CLTS, visualized using a circular violin plot. The approach is applied to three real datasets to demonstrate its utility in handling outliers in circular data.  
DOMAIN: circular statistics  
STRUCTURE: other: statistical estimation  
DATA_OBJECT: point set  
INFERENCE: deterministic or closed-form  
PROBLEM_FORM: estimation  
DISTRIBUTION: continuous; continuous  
COMPLEXITY: not stated  
DATA_AVAILABILITY: none  
CODE_AVAILABILITY: none  
PREREGISTRATION: none  
EVIDENCE_BASIS: empirical-with-private-data
