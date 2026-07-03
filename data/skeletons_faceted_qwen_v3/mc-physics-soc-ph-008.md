MECHANISM: The paper computes a geospatial simulation of agent behavior, disease transmission, and pathogen shedding. Agents are initialized with attributes and needs, including a defecation need modeled as a physiological process. Agents move through a network of locations (homes, workplaces, public venues) based on behavioral rules and needs. At each time step, agents perform activities, interact with others, and shed pathogens if infected. Pathogen shedding is modeled as a function of infection status and time since infection. Defecation events are triggered by the accumulation of the defecation need, with agents selecting toilet locations based on proximity and availability. Pathogen loads from defecation events are aggregated into a sewer network model, which tracks spatial and temporal dynamics of contamination. Disease transmission occurs through co-location and social interactions, with infection states (susceptible, exposed, infectious, recovered) updated based on contact rates and shedding dynamics. The simulation integrates mobility patterns, social networks, and environmental factors to generate wastewater signals. Outputs include spatial-temporal pathogen distributions, epidemic curves, and population-level disease metrics. The model is parameterized with distributions for agent attributes, shedding rates, and mobility patterns, and validated through case studies with synthetic populations.
DOMAIN: wastewater-based epidemiology
STRUCTURE: other: agent-based simulation
DATA_OBJECT: graph or network
INFERENCE: deterministic or closed-form
PROBLEM_FORM: simulation or generation
DISTRIBUTION: continuous; continuous
COMPLEXITY: not stated
DATA_AVAILABILITY: public-repository
CODE_AVAILABILITY: public-repository
PREREGISTRATION: none
EVIDENCE_BASIS: simulation-study
