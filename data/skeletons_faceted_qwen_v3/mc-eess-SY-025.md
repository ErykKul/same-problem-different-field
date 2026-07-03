MECHANISM: The paper computes a robust nonlinear model predictive control (NMPC) strategy to regulate a dynamic system under parametric uncertainty and time-varying constraints. The system is modeled as a nonlinear differential equation with state variables representing concentrations of biochemical species and inputs as flow rates of co-feedstocks. The control objective is to minimize a weighted tracking error between predicted outputs and reference trajectories while enforcing state and input constraints. The method introduces a "tube" formulation, where a nominal system (without disturbances) is solved first, and an ancillary problem adjusts for bounded disturbances by re-evaluating the nominal trajectory at each control step. The optimization problem includes a cost function penalizing deviations from reference outputs, state-input constraints, and terminal costs. The nominal and ancillary problems are solved sequentially, with the ancillary problem using the nominal solution as a reference but allowing adjustments based on current measurements. The method ensures recursive feasibility and constraint satisfaction by bounding disturbances and tightening constraints in the nominal problem. The system dynamics are described by ordinary differential equations (ODEs) with nonlinear terms arising from kinetic rate expressions. The control horizon and prediction horizon are distinct, with the control horizon shorter to reduce computational load. The solution involves solving a constrained optimization problem at each time step, using the current state estimate and updated reference trajectories. The method is validated through numerical simulations that mimic real-world operational conditions.  
DOMAIN: nonlinear process control  
STRUCTURE: dynamic programming  
DATA_OBJECT: continuous function or field  
INFERENCE: deterministic or closed-form  
PROBLEM_FORM: optimization  
DISTRIBUTION: none  
COMPLEXITY: not stated  
DATA_AVAILABILITY: none  
CODE_AVAILABILITY: none  
PREREGISTRATION: none  
EVIDENCE_BASIS: simulation-study
