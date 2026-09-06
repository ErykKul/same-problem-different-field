# Blind judging instruction (wild three-arm study)

You will read pairs of research papers from two different fields. For each pair you see only the two field
labels and the two abstracts (truncated to about 550 characters). You do not know how the pair was selected.

Question, per pair: is this pair a genuine cross-domain solution-import candidate?

Answer YES only if the two papers solve the same underlying computational problem: the same specific
mathematical or algorithmic core (the same kind of object being estimated, optimized, inferred, or
transformed, by the same kind of procedure), such that a standard solver or estimator from one paper's field
could be applied to the other paper's problem after renaming the variables.

Answer NO if the shared ground is only a broad paradigm ("both use machine learning", "both are optimization
problems", "both analyze time series"), only a shared application topic, or if either paper has no
computational method of its own (a survey, a position paper, a framework description, a data release).

Judge from the text alone. Do not search the web or look up the papers. When the abstracts do not give
enough information to establish the same specific core, answer NO.

Output: a JSON array with one object per pair, in input order:
{"id": <id>, "genuine": true|false, "reason": "<at most 15 words>"}
Return only the JSON array, nothing else.
