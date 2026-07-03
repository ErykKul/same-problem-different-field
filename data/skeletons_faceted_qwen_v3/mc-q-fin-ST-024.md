MECHANISM: The paper constructs a multi-agent system where four analytical agents (announcement, event, price momentum, market) process structured data from distinct dimensions. Each agent generates quantifiable signals through rule-based technical indicators, historical impact analysis, and macroeconomic state classification. These signals are aggregated by a prediction agent into multi-horizon directional probability distributions using a large language model (LLM) for joint reasoning. A decision agent maps these probabilistic outputs into discrete position adjustment signals under risk constraints, forming a closed-loop system. The prediction layer compares two model pathways: (i) a general-purpose LLM (e.g., DeepSeek-R1) directly applied to structured context, and (ii) a fine-tuned small LLM (e.g., Qwen3-8B) trained via supervised fine-tuning and reinforcement learning on historical data. The system employs dynamic volatility thresholds to define "sideways" price movements, scales thresholds across time horizons using square root of time rules, and synthesizes technical, event, and macroeconomic signals into structured contexts for LLM reasoning. Backtesting evaluates cumulative return, Sharpe ratio, and maximum drawdown against a buy-and-hold benchmark. The framework emphasizes structured reasoning, evidence-based decision logic, and alignment with trading principles through post-training optimization.  
DOMAIN: financial systems and trading strategies  
STRUCTURE: map-reduce or embarrassingly-parallel  
DATA_OBJECT: graph or network  
INFERENCE: deterministic or closed-form  
PROBLEM_FORM: prediction or classification  
DISTRIBUTION: continuous; continuous  
COMPLEXITY: polynomial iterative  
DATA_AVAILABILITY: dataset-in-repository  
CODE_AVAILABILITY: public-repository  
PREREGISTRATION: none  
EVIDENCE_BASIS: empirical-with-released-data
