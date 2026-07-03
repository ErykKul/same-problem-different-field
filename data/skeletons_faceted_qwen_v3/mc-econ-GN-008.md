MECHANISM: The paper computes statistical relationships between AI exposure and labor market outcomes using regression models and hypothesis testing. It begins by aggregating employment and unemployment counts across occupations, states, and time periods to calculate an unemployment risk metric as a function of employment and unemployment numbers. This risk is scaled using a formula that combines weekly unemployment data with annual employment statistics. The paper then applies ordinary least squares regression to estimate how unemployment risk varies with AI exposure, using interaction terms to model differences between low- and high-exposure occupations over time. It also computes job-seeking delays for college graduates by analyzing LinkedIn profiles, estimating delays as the time between degree completion and first job start, while controlling for factors like job opening rates, field of study, and university. A separate analysis derives education exposure scores from syllabi data by computing semantic similarity between course objectives and AI-related tasks, then aggregates these scores across a worker’s academic history. The paper performs hypothesis tests to compare job gaps between graduation cohorts, using the Delta method to approximate sampling variability and compute z-scores for significance testing. It also conducts weighted analyses to align LinkedIn data with population-representative benchmarks from the National Survey of College Graduates. All computations rely on statistical inference from observational data rather than simulation or algorithmic prediction.  
DOMAIN: labor economics and AI impact analysis  
STRUCTURE: empirical statistical analysis  
DATA_OBJECT: dataset  
INFERENCE: frequentist point estimate  
PROBLEM_FORM: estimation  
DISTRIBUTION: none  
COMPLEXITY: not stated  
DATA_AVAILABILITY: dataset-in-repository  
CODE_AVAILABILITY: public-repository  
PREREGISTRATION: none  
EVIDENCE_BASIS: empirical-with-private-data
