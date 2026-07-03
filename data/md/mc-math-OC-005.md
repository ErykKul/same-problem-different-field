# Safe Adaptive Feedback Control via Barrier States

## Abstract

This paper presents a safe feedback control framework for nonlinear control-affine systems with parametric uncertainty by leveraging adaptive dynamic programming (ADP) with barrier-state augmentation. The developed ADP-based controller enforces control invariance by optimizing a value function that explicitly penalizes the barrier state, thereby embedding safety directly into the Bellman structure. The near-optimal control policy computed using model-based reinforcement learning is combined with a concurrent learning estimator to identify the unknown parameters and guarantee uniform convergence without requiring persistency of excitation. Using a barrier-state Lyapunov function, we establish boundedness of the barrier dynamics and prove closed-loop stability and safety. Numerical simulations on an optimal obstacle-avoidance problem validate the effectiveness of the developed approach.
