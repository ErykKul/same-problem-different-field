MECHANISM: Several alternative scoring instruments assign a real-valued index to each member of a large collection of entities, where each index is derived by aggregating counts of directed links pointing into that entity from other entities. One instrument computes a threshold-style summary, the largest integer such that at least that many of an entity's items each received at least that many incoming links. The procedure assembles three separately produced tables of such indices for overlapping but non-identical universes of entities. Entities are matched across the tables by label to extract the common subset present in all three. For each pair of instruments, the matched entities are ranked by their respective indices and a rank-based association coefficient is computed from the differences in paired ranks. The resulting coefficients quantify the monotone agreement between the orderings produced by different instruments. Significance of each coefficient is assessed against the null of no association. Larger coefficients indicate that two instruments order the entities almost identically despite differing aggregation rules and coverage. The analysis also contrasts size-sensitive aggregates against size-normalized ones to explain ordering discrepancies for outlier entities.
DOMAIN: bibliometrics and journal evaluation in scientometrics
STRUCTURE: other: rank correlation
DATA_OBJECT: set or table
INFERENCE: frequentist point estimate
PROBLEM_FORM: ranking or retrieval
DISTRIBUTION: ordinal; nonparametric
COMPLEXITY: closed-form
