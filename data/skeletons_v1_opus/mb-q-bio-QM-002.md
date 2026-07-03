MECHANISM: The system automates building a predictive model from heterogeneous tabular collections through two coupled stages. First, a frozen large language model is prompted with raw field descriptors to infer a canonical mapping specification that aligns inconsistent schemas and naming into one interface, then executes that mapping to normalize the inputs. Second, a tree search over a structured, three-level action space (modeling paradigm, then architecture family, then optimization refinements) searches for a configuration whose statistical assumptions match the data. Each search step selects a node by an upper-confidence rule mixing maximum and average observed reward, expands it by instantiating a candidate via the language model, simulates it by running a full training-and-validation cycle, and backpropagates statistics up the tree. Retrieval of analogous prior cases warm-starts the tree when similarity exceeds a threshold and is bypassed otherwise to avoid negative transfer. The reward combines a normalized predictive-fidelity score with an execution-time penalty. The chosen model maps an input observation and an intervention label to a predicted post-intervention response distribution, scored by error and correlation of the shift vectors. The procedure is fully closed-loop with no manual intervention.
DOMAIN: single-cell perturbation modeling in biology
STRUCTURE: graph traversal
DATA_OBJECT: tree or hierarchy
INFERENCE: deterministic optimization
PROBLEM_FORM: search
DISTRIBUTION: count; none
COMPLEXITY: not stated
