MECHANISM: The paper computes a coupled system of epidemic spread and vaccination behavior using a modified SIRS model with additional states for vaccination and mutant strain infection. The model defines five states (S, V, I₁, I₂, R) and transitions between them based on probabilities derived from evolutionary game theory. Individuals choose vaccination strategies by comparing payoffs from vaccination versus non-vaccination, with payoffs determined by vaccine efficacy, cost, infection risk, and neighborhood interactions. Payoff calculations integrate local game outcomes with global epidemic factors like herd immunity and infection density. A microscopic Markov chain approach (MMCA) couples the epidemic dynamics with vaccination strategy updates, using a Fermi rule for strategy adoption based on payoff differences. Transition probabilities between states are computed using weighted network interactions, with infection rates adjusted by vaccination status. The model incorporates mutation from I₁ to I₂ at a rate μ and recovery rates γ₁, γ₂ for each strain. Immunity loss from recovered individuals reintroduces them to the susceptible state. The system evolves through differential equations derived from state transition probabilities, with parameters including conformity coefficients, mutation rates, and network weights. Sensitivity analysis identifies vaccine cost, efficacy, and perceived risk as key drivers of vaccination uptake. The framework simulates outbreak mitigation across scenarios by adjusting these parameters.  
DOMAIN: epidemiology and evolutionary game theory  
STRUCTURE: other: compartmental model  
DATA_OBJECT: graph or network  
INFERENCE: deterministic or closed-form  
PROBLEM_FORM: prediction or classification  
DISTRIBUTION: count; continuous  
COMPLEXITY: not stated  
DATA_AVAILABILITY: none  
CODE_AVAILABILITY: none  
PREREGISTRATION: none  
EVIDENCE_BASIS: simulation-study
