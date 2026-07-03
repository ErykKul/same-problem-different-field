MECHANISM: The paper computes a joint estimation of attitude, angular velocity, and sensor misalignment using a two-layer framework. The first layer is a 9-state error-state Kalman filter that estimates attitude (as a unit quaternion), angular velocity, and gyroscope bias. The second layer is a Bayesian multiple-model adaptive estimator that operates on a discrete grid of misalignment hypotheses. The Kalman filter uses a multiplicative error state formulation to handle the non-Euclidean nature of quaternions, with the error state consisting of angular velocity deviations, bias deviations, and small-angle attitude errors represented as Modified Rodrigues Parameters (MRPs). The filter predicts the state by linearizing the dynamics around the nominal trajectory, using a block-lower-triangular state transition matrix derived from the system Jacobians. Measurement updates are performed using TRIAD-based attitude observations, which compute a direction cosine matrix from two inertial reference vectors and their noisy body-frame measurements. The residual between the predicted and measured attitude is converted into an MRP vector, and the angular velocity residual is computed as the difference between the measured and predicted values. The Kalman gain is derived from the innovation covariance and the prior error covariance, and the state and covariance are updated accordingly. The Bayesian layer maintains a grid of misalignment hypotheses, updating model probabilities based on the likelihood of the current measurement. A diversity metric triggers adaptive refinement of the grid around a weighted mean estimate, concentrating computation in the most probable region of the parameter space. The framework avoids nonlinear state augmentation for misalignment and supports parallel implementation, ensuring computational efficiency for onboard processors.  
DOMAIN: spacecraft attitude estimation  
STRUCTURE: other: multi-model adaptive estimation  
DATA_OBJECT: grid  
INFERENCE: Bayesian posterior  
PROBLEM_FORM: estimation  
DISTRIBUTION: continuous; Gaussian  
COMPLEXITY: not stated  
DATA_AVAILABILITY: none  
CODE_AVAILABILITY: none  
PREREGISTRATION: none  
EVIDENCE_BASIS: simulation-study
