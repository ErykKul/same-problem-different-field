MECHANISM: The paper computes a Bayesian hierarchical model to assess the efficacy of targeted therapies in basket trials with delayed outcomes. It begins by defining a binary response variable for each patient, modeled as a Bernoulli distribution with a parameter representing the response rate. A conjugate Beta prior is assigned to this parameter, and the posterior distribution is updated iteratively as patients are enrolled. To handle information sharing across baskets, the method calculates similarity between posterior distributions using Jensen-Shannon Divergence, assigning weights based on this similarity. These weights determine the extent of information borrowing across baskets. For delayed outcomes, the model incorporates multiple imputation using a Weibull survival model to estimate missing responses. The imputation process involves sampling parameters from the posterior distribution, generating imputed responses based on the survival model, and recalculating posterior distributions with the imputed data. The method then computes the posterior probability of futility for each basket, comparing it to a predefined threshold to decide whether to stop the trial. The process is repeated across multiple imputation iterations to account for uncertainty in the missing data. The final decision to stop or continue the trial is based on the average posterior probability across all imputations. The approach balances computational efficiency with the need to handle delayed outcomes and missing data in a statistically rigorous manner.

DOMAIN: clinical trial statistics

STRUCTURE: Bayesian posterior

DATA_OBJECT: set or table

INFERENCE: Bayesian posterior

PROBLEM_FORM: decision or test

DISTRIBUTION: binary; Weibull

COMPLEXITY: not stated

DATA_AVAILABILITY: dataset-in-repository

CODE_AVAILABILITY: public-repository

PREREGISTRATION: none

EVIDENCE_BASIS: simulation-study
