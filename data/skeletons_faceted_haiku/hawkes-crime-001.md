MECHANISM: Model a stream of timestamped, located events as a point process whose conditional intensity is a constant background rate plus a sum of triggering contributions from past events. Each past event raises the short-term rate of nearby future events through a triggering kernel that decays in time and in space. Decompose the intensity into the stationary background and the event-triggered part, and estimate both nonparametrically. Estimation alternates between probabilistically attributing each event to either the background or a specific earlier parent event, and re-estimating the background rate and the triggering kernel density from those soft attributions. Iterating this attribute-then-reestimate scheme converges to the maximum-likelihood decomposition of observed from triggered events.
DOMAIN: criminology
STRUCTURE: other: self-exciting point process
DATA_OBJECT: point set
INFERENCE: frequentist point estimate
PROBLEM_FORM: estimation
DISTRIBUTION: count; conditional-intensity point process
COMPLEXITY: polynomial iterative
DATA_AVAILABILITY: data-on-request
CODE_AVAILABILITY: none
PREREGISTRATION: none
EVIDENCE_BASIS: empirical-with-private-data
