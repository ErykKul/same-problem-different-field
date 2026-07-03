MECHANISM: Constructs four specialized analytical agents (announcement, event, price momentum, market) that compute domain-specific indicators and structured signals; aggregates indicators into language-model-readable context with multi-layer representation (raw, interpretation, state labels); feeds agent outputs to prediction agent which generates multi-horizon directional probability distributions via LLM inference; supplies predictions and current account state to decision agent which outputs discrete position adjustment signals; executes trades and recomputes account status; compares two implementations: DeepSeek-R1 (general-purpose) for prediction versus fine-tuned Qwen3-8B (supervised fine-tuning plus GSPO reinforcement learning alignment); evaluates via backtest on daily OHLCV data with transaction costs.
DOMAIN: Multi-agent large language model investment system for real estate investment trusts
STRUCTURE: other: multi-agent system
DATA_OBJECT: sequence or time-series
INFERENCE: sampling or Monte-Carlo
PROBLEM_FORM: decision or test
DISTRIBUTION: none
COMPLEXITY: not stated
