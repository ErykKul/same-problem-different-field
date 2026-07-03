MECHANISM: The paper derives analytic expressions for degree distributions in networks that grow by adding edges to a fixed number of vertices, using both linear and non-linear preferential attachment rules. It defines a probability function $ P(k,t,\gamma) $ for vertex degree $ k $ at time $ t $, parameterized by $ \gamma $, and derives recurrence relations for auxiliary functions $ F(k,t,\gamma) $ that encode the attachment dynamics. For linear attachment ($ \gamma=1 $), it solves the recurrence using generating functions, leading to a closed-form expression for $ P(k,t,1) $ that decays exponentially with $ k $. For non-linear attachment ($ 0 < \gamma < 1 $), it shows the degree distribution also decays exponentially, despite the absence of an exact closed-form solution. The analysis involves approximating sums with logarithmic functions, manipulating gamma functions, and bounding products of terms involving $ \gamma $. The conclusion is that preferential attachment alone, without vertex growth, produces exponential decay in degree distributions rather than power-law behavior. The method relies on asymptotic analysis for large $ n $ and $ t $, and uses mathematical transformations to simplify recurrence relations. The paper contrasts these results with models that include both vertex and edge growth, which produce scale-free or stretched-exponential distributions. The core computation is the derivation of degree distributions through recurrence relations and generating functions, with emphasis on asymptotic behavior and parameterized attachment rules.
DOMAIN: network theory and scale-free networks
STRUCTURE: other: mathematical derivation
DATA_OBJECT: continuous function or field
INFERENCE: deterministic or closed-form
PROBLEM_FORM: characterization
DISTRIBUTION: continuous; exponential
COMPLEXITY: not stated
DATA_AVAILABILITY: none
CODE_AVAILABILITY: none
PREREGISTRATION: none
EVIDENCE_BASIS: mathematical-proof
