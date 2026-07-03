MECHANISM: Architecture framework for low-altitude economy (LAE) orchestration using open radio access network (O-RAN). Operationalizes two control loops: Non-RT RIC executes long-term policy learning and model training on historical data; Near-RT RIC executes real-time closed-loop control via xApps that ingest sensor telemetry and network KPIs to generate trajectory decisions. In use case study: preprocess aerial imagery via ResNet for semantic feature extraction (rApp); formulate multi-UAV trajectory optimization as constrained Markov decision process; solve via multi-agent deep deterministic policy gradient (MADDPG) to maximize cumulative reward subject to collision-avoidance, QoS, and mission constraints.
DOMAIN: Telecommunications, unmanned aerial systems, network control
STRUCTURE: other: reinforcement learning policy optimization
DATA_OBJECT: sequence or time-series
INFERENCE: sampling or Monte-Carlo
PROBLEM_FORM: control
DISTRIBUTION: none
COMPLEXITY: not stated
