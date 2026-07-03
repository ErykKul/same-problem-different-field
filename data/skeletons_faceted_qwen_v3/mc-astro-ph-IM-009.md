MECHANISM: The paper describes the development of a web-based platform for interactive visualization of multivariate astronomical time series data. The system allows users to explore and compare light curves from transient events and low-mass active galactic nuclei (AGNs), with features including search functionality, parameter display, and interactive plots. The backend processes data using existing algorithms (e.g., neural networks and Gaussian processes) for light curve approximation and variability analysis, but the paper does not present a novel computational method or algorithm. The architecture includes a Python-based FastAPI server, MongoDB for data storage, and Docker containers for deployment. The frontend uses Plotly for interactive graphics, and the system supports data ingestion through scripts that map processed results into internal structures. The platform is demonstrated with real observational datasets, including ZTF and ATLAS forced photometry data, and provides tools for post-processing light curves. The paper emphasizes the system's usability for scientific discovery but does not claim to advance the underlying computational techniques for light curve analysis.  
DOMAIN: astronomical data visualization  
STRUCTURE: none  
DATA_OBJECT: none  
INFERENCE: none  
PROBLEM_FORM: visualization  
DISTRIBUTION: none  
COMPLEXITY: none  
DATA_AVAILABILITY: public-benchmark-used  
CODE_AVAILABILITY: public-repository  
PREREGISTRATION: none  
EVIDENCE_BASIS: empirical-with-released-data
