MECHANISM: Records are assembled by merging several registries with scraped archival snapshots into a deduplicated inventory of entities and their machine endpoints, with categorical types harmonized to a common vocabulary. Each entity address and endpoint is probed for a response status code, and codes are tabulated to classify entities as live or defunct, with a sub-class flagged by an address-level redirect that is not mirrored at the endpoint. For defunct entities, an approximate time of failure is recovered from the last archived snapshot. Cumulative counts of failures over time are then fit by both a linear and a log-linear model, and goodness of fit is compared to judge additive versus multiplicative growth; a geometric decay model with a constant per-period rate is fit to project the surviving population forward. A large external corpus is queried to extract textual references whose address prefixes match defunct entities, counting how many works refer to defunct content and, combining failure dates with publication dates, how many references were already defunct at publication. Outputs are descriptive counts, proportions, central-tendency summaries, and the fitted slopes and decay rate. A simple regression of failure proportion on a regional axis tests for association.
DOMAIN: scholarly repository infrastructure and bibliometrics
STRUCTURE: other: tabulation and curve fitting
DATA_OBJECT: set or table
INFERENCE: frequentist point estimate
PROBLEM_FORM: estimation
DISTRIBUTION: count; none
COMPLEXITY: closed-form
