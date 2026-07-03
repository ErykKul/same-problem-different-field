MECHANISM: Given two finite sequences of symbols, the method fills a two-dimensional table indexed by prefix lengths of the two inputs, where each cell holds an extremal accumulated score. Each cell is computed by a recurrence that takes the maximum over a small fixed set of candidate values derived from its immediate upper, left, and upper-left neighbors plus a local pairwise scoring term. Auxiliary tables track penalties for consecutive insertions so that the cost of a run of skips is an affine function of its length. The recurrence is evaluated in an order that respects these neighbor dependencies, so cells along an anti-diagonal can be updated concurrently while preserding the dependency on previously computed rows. To bound memory the table is partitioned into vertical bands processed in stages, with only boundary columns carried between stages, giving linear space for score-only evaluation. The single optimal value is read from a designated terminal cell or from the extremum over a final row or column depending on the chosen boundary initialization. An optional back-pointer trace reconstructs the actual extremal path, using a divide-and-conquer midpoint scheme to keep space linear at the cost of recomputing cells. The dominant cost is the product of the two sequence lengths in additions and maximum operations per cell.
DOMAIN: bioinformatics, genomic sequence alignment
STRUCTURE: dynamic programming
DATA_OBJECT: sequence or time-series
INFERENCE: deterministic optimization
PROBLEM_FORM: optimization
DISTRIBUTION: none; none
COMPLEXITY: polynomial iterative
