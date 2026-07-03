MECHANISM: For each entity a radius-ordered sequence of paired measurements (a position coordinate and an associated rate) is taken as input. A single scalar correction constant is computed in closed form from only the innermost and outermost members of the sequence, as the difference of two ratio terms in which one term is rescaled by a power-law factor of the position ratio. This constant is then used in a per-member closed-form transformation that subtracts a linear-in-position correction from each observed rate to yield a baseline-adjusted quantity. A separate closed-form recurrence reconstructs an expected baseline profile anchored at the first member and propagated outward using the same power-law scaling. The resulting fitted profile is compared point-by-point against the observed sequence, and goodness-of-fit is summarized by root-mean-square residual and a coefficient-of-determination statistic. The procedure is repeated independently across many entities, and the per-entity fit statistics are tabulated and contrasted against two alternative parametric baseline models. No iterative optimization or parameter search is performed; every output follows algebraically from the input measurements.
DOMAIN: astrophysics, galaxy rotation kinematics
STRUCTURE: other: closed-form curve fit
DATA_OBJECT: sequence or time-series
INFERENCE: deterministic or closed-form
PROBLEM_FORM: estimation
DISTRIBUTION: continuous; none
COMPLEXITY: closed-form
