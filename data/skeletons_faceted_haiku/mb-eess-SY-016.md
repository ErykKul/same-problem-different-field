MECHANISM: A control framework coordinates vehicle maneuvers in mixed traffic networks where buses and connected/automated vehicles share dedicated lanes. The approach segments each network edge into upstream/downstream portions and predicts vehicle arrivals using constant-speed forecasting. For buses, a predictive protection window prevents vehicle conflicts within a specified temporal horizon. Lane-change decisions are evaluated per segment using a weighted utility function combining travel time benefits (Bureau of Public Roads flow-delay model), routing feasibility constraints, and penalties for excessive maneuvering. When predicted bus travel time exceeds tolerance, targeted rerouting via shortest-path search reduces CAV inflow to protected segments. The framework enforces hard constraints to ensure buses exit protected segments before allowing CAV entry, and selects at most one vehicle per segment per control step.
DOMAIN: Traffic control for mixed autonomous/conventional vehicle corridors
STRUCTURE: other: predictive segment-level coordination with optimization
DATA_OBJECT: graph or network
INFERENCE: deterministic or closed-form
PROBLEM_FORM: control
DISTRIBUTION: none
COMPLEXITY: polynomial iterative
