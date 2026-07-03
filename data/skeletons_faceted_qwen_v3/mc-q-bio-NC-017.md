MECHANISM: The paper defines a hierarchy of information-processing systems based on their ability to transform input into output through three ordered classes. Class I systems map inputs directly to outputs without memory or internal state, using a time-varying gain or bias. Class II systems incorporate internal states that retain memory of past inputs, applying a fixed transformation operator to reshape or filter input. Class III systems extend Class II by allowing the transformation operator itself to evolve over time as a function of prior system activity, enabling self-modulation. The framework distinguishes these classes through mathematical equations: Class I uses $ R(t) = \alpha(t)I(t) + \varepsilon(t) $, Class II applies a fixed transformation $ R(t) = \mathcal{T}[I(t)] + \varepsilon(t) $, and Class III introduces recursion via $ \mathcal{T}_{t+1} = \mathcal{G}(\mathcal{T}_t, R_t) $. These equations capture how input is transformed, with Class III systems adapting their transformation rules based on historical outputs. The hierarchy is used to identify necessary informational conditions for agency, where adaptivity in transformation rules (Class III) is a key criterion. Examples include thermostats (Class I), memristors (Class II), and neural networks (Class III). The framework is substrate-independent, focusing on intrinsic dynamics rather than application-specific details.  
DOMAIN: information processing and agency  
STRUCTURE: other: information-processing hierarchy  
DATA_OBJECT: system's information-processing dynamics  
INFERENCE: deterministic or closed-form  
PROBLEM_FORM: classification  
DISTRIBUTION: none  
COMPLEXITY: not stated  
DATA_AVAILABILITY: none  
CODE_AVAILABILITY: none  
PREREGISTRATION: none  
EVIDENCE_BASIS: mathematical-proof
