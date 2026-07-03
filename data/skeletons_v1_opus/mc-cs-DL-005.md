MECHANISM: Each record is reduced to a single text string by concatenating its descriptive fields and applying lightweight normalization that lowercases and strips punctuation while preserving logical operators and wildcard tokens. A curated library associates each category with a set of logical sub-expressions, each built from conjunctions, disjunctions, and prefix-wildcard term patterns. For every record and every category, each sub-expression is evaluated as a deterministic boolean predicate against the normalized string, counting a match when its conditions are satisfied. A relevance score per category is computed as the ratio of matched sub-expressions to the total defined for that category. Categories are ranked by this normalized score and the top-N are returned, with N user-selectable. The procedure is fully deterministic and produces identical outputs for identical inputs, and it records which sub-expressions fired so each assignment is traceable. Evaluation compares the top-N predictions against manually assigned ground-truth labels on a controlled balanced set, scoring a hit when the true label appears among the returned categories. Accuracy is reported as a function of N across categories, and error patterns are attributed to overlap among category scopes rather than spurious term matches.
DOMAIN: bibliometric text classification by policy goals
STRUCTURE: finite-state machine
DATA_OBJECT: set or table
INFERENCE: deterministic or closed-form
PROBLEM_FORM: prediction or classification
DISTRIBUTION: none; none
COMPLEXITY: closed-form
