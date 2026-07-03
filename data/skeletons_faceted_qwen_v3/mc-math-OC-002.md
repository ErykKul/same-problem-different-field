MECHANISM: The paper computes the difference between two detection probabilities for a search plan that optimizes subjective detection. It defines a detection function $d(x,y)$, which maps effort $y$ allocated to location $x$ to a probability of detecting a target. The subjective detection probability $P[f]$ is computed as the integral (or sum) of $d(x,f(x))$ weighted by a target distribution $\pi(x)$, where $f(x)$ is the effort allocation. The true detection probability $P^{\#}[f]$ is defined as $d(x_0,f(x_0))$, where $x_0$ is the actual target location. The uniformly optimal search plan $\varphi^{\star}$ maximizes $P[f]$ at each time $t$, subject to a constraint on total effort $E(t)$. This involves solving an optimization problem where the allocation function $\varphi(x,t)$ is derived from inverting a function $Q(\lambda)$, which aggregates the derivative of $d(x,y)$ scaled by $\pi(x)$. The paper provides examples showing that $P[f]$ and $P^{\#}[f]$ may or may not coincide, and proves that $P^{\#}[f]$ converges to 1 as search time increases. It also establishes that using a composite prior can lead to suboptimal true detection probabilities. The computation involves solving integral equations, inverting functions, and analyzing convergence properties of the optimization solution. The method relies on regularity conditions of $d(x,y)$, such as monotonicity and differentiability, to ensure existence and uniqueness of the optimal plan. The paper does not introduce new algorithms but applies existing optimization frameworks to a specific problem in search theory.

DOMAIN: optimal search theory

STRUCTURE: optimization

DATA_OBJECT: continuous function

INFERENCE: deterministic or closed-form

PROBLEM_FORM: optimization

DISTRIBUTION: none

COMPLEXITY: not stated

DATA_AVAILABILITY: none

CODE_AVAILABILITY: none

PREREGISTRATION: none

EVIDENCE_BASIS: mathematical-proof
