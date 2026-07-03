MECHANISM: An election is represented as a bipartite graph with voter and candidate nodes connected by weighted edges representing preference scores. A graph neural network learns a permutation-equivariant function over this graph to output a probability distribution over candidates (the voting rule). The network is trained to maximize an objective function (e.g., social welfare) via gradient descent. A second strategy module, trained adversarially, learns to manipulate preference scores (strategic voting) to maximize individual utility given knowledge of the voting rule. Both modules are jointly trained: the voting rule adapts to strategic behavior while satisfying anonymity and neutrality constraints.
DOMAIN: Voting theory and mechanism design with machine learning
STRUCTURE: graphical models
DATA_OBJECT: graph or network
INFERENCE: optimization only
PROBLEM_FORM: optimization
DISTRIBUTION: none
COMPLEXITY: not stated
