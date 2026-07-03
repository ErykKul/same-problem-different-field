MECHANISM: The paper computes a combined control strategy for legged robots with manipulator arms, integrating model-based admittance control and reinforcement learning (RL). The admittance controller maps external wrenches (force and torque) into desired end-effector velocities using a stiffness-damping relationship, defined by $\mathcal{W} - \mathcal{W}' = \mathbf{K}\log(\mathbf{x}_{ee}^{\prime w\top}\mathbf{x}_{ee}^{w}) + \mathbf{D}[\mathbf{v}_{ee}^w, \boldsymbol{\omega}_{ee}^w]$, where $\mathbf{K}$ and $\mathbf{D}$ are stiffness and damping matrices. These velocities are tracked by the arm and leg controllers, which compute joint velocities via the damped pseudo-inverse of the Jacobian: $\dot{\mathbf{q}}_{arm} = \mathbf{J}^{\#}[\mathbf{v}_{ee}^b, \boldsymbol{\omega}_{ee}^b]$. A Kalman filter enhanced with neural networks estimates base velocities by modeling system dynamics and incorporating state covariance from the filter into the RL policy's observations. The RL policy learns to control the base motion by optimizing a reward function that includes terms for tracking desired end-effector velocities, energy efficiency, and locomotion quality. The Reference Governor (RG) enforces safety constraints by adjusting the reference wrench $\mathcal{W}'$, and the admittance controller ensures compliance during contact interactions. The Kalman filter's prediction and update steps incorporate process noise modeled by a neural network, with covariance matrices $\mathbf{Q}_t$ and $\mathbf{P}_t$ derived from the network's output. The system operates in continuous time, with state estimation and control updates occurring at each time step.  
DOMAIN: robotics: whole-body loco-manipulation  
STRUCTURE: other: model-based and learning-based control  
DATA_OBJECT: continuous function or field  
INFERENCE: Bayesian posterior  
PROBLEM_FORM: control  
DISTRIBUTION: none  
COMPLEXITY: not stated  
DATA_AVAILABILITY: none  
CODE_AVAILABILITY: none  
PREREGISTRATION: none  
EVIDENCE_BASIS: empirical-with-private-data
