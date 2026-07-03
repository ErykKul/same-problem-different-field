export const meta = {
  name: 'perturbation-test-2x2',
  description: 'Interventional structure-vs-surface test: re-skin (keep computation) + math-edit (keep domain) each paper, distill all three, return BOTH the rewrites (for the abstract baseline) and the fingerprint skeletons',
  phases: [{ title: 'Rewrite' }, { title: 'Distill' }],
}

const ROOT = process.env.RDR_ROOT || '.'   // package root
const IDS = ['kalman-control-001','em-astro-001','eigen-ecology-001','fft-astro-distractor-001','pca-causal-001','sparse-finance-001','fft-astro-001','hmm-ecology-002','dp-bio-001','mcmc-cosmo-001']

const DISTILL = `You are reducing a paper to a STRUCTURED COMPUTATIONAL FINGERPRINT: facets each on their own line with the EXACT label. Two papers from different fields using the SAME computation must agree on these facets even when topics differ. FIRST decide if the paper COMPUTES something; if it is qualitative/survey/no-method write "none" for STRUCTURE, DATA_OBJECT, INFERENCE, DISTRIBUTION, COMPLEXITY and one sentence for MECHANISM. Controlled facets (STRUCTURE, DATA_OBJECT, INFERENCE, PROBLEM_FORM) are EXACTLY ONE short value; if nothing fits write "other: <term>". Do NOT name a method/algorithm/software in any facet. Output EXACTLY these labeled lines, nothing else:
MECHANISM: <6-12 sentence domain-neutral skeleton of WHAT is computed and the steps in order, in generic math language; strip ALL domain/application/dataset words (use "an entity", "a quantity"); do NOT name famous methods unless unavoidable.>
DOMAIN: <subject area, 3-8 words; the ONLY facet that may name the field.>
STRUCTURE: <dominant computational pattern, one short term, e.g. dense/sparse linear algebra, spectral or transform, graph traversal, dynamic programming, graphical models, kernel method, numerical optimization, MCMC sampling, or "other: <term>".>
DATA_OBJECT: <one of: dense matrix or tensor, sparse matrix, grid or lattice, mesh, graph or network, point set, sequence or time-series, tree or hierarchy, set or table, continuous function or field, none.>
INFERENCE: <one of: deterministic or closed-form, frequentist point estimate, maximum likelihood, bayesian posterior, variational, sampling or Monte-Carlo, bootstrap or resampling, deterministic optimization, none.>
PROBLEM_FORM: <one of: estimation, prediction or classification, optimization, decision or test, search, counting, simulation or generation, proof or characterization, control, ranking or retrieval, reconstruction or denoising, none.>
DISTRIBUTION: <"<measured>; <assumed>", one coarse token per side, or none.>
COMPLEXITY: <one of: closed-form, polynomial iterative, combinatorial or NP-hard, consistency, finite-sample bound, convergence rate, regret bound, not stated.>`

const RW_SCHEMA = { type:'object', additionalProperties:false, properties:{ id:{type:'string'}, reskin:{type:'string'}, math:{type:'string'} }, required:['id','reskin','math'] }
const SK_SCHEMA = { type:'object', additionalProperties:false, properties:{ id:{type:'string'}, s_orig:{type:'string'}, s_reskin:{type:'string'}, s_math:{type:'string'} }, required:['id','s_orig','s_reskin','s_math'] }

phase('Rewrite')
const rw = await parallel(IDS.map((id) => () => agent(`Use Read to read ${ROOT}/data/md/${id}.md (a research paper's title + abstract). Produce TWO rewrites of it, each 120-180 words in the same scholarly style:
1. RESKIN: rewrite into a CLEARLY DIFFERENT field and application, keeping the underlying COMPUTATION / METHOD / MATH IDENTICAL (same algorithm, same estimator, same data structure; only the domain words, application, dataset, and motivation change). The computation a reader would extract must be unchanged.
2. MATH-EDIT: keep the SAME field, topic, dataset, and application words, but CHANGE the underlying computation to a genuinely DIFFERENT method (swap the estimator / objective / data structure for a different one). The surface stays in the same field; the math becomes a different computation.
Return {id:"${id}", reskin, math}.`, { label:`rw:${id}`, phase:'Rewrite', model:'sonnet', schema:RW_SCHEMA })))
// NOTE: the rewriter (Sonnet) is a DIFFERENT model from the distiller (Haiku, below), so the
// counterfactuals are not authored by the same model that produces the fingerprint. This rules out the
// "invariance is just an in-distribution artifact of one model" confound that a single-model design invites.

phase('Distill')
const sk = await parallel(IDS.map((id, i) => () => agent(`Apply the following distillation prompt SEPARATELY to three texts and return the three resulting facet blocks verbatim.

DISTILLATION PROMPT:
${DISTILL}

TEXT 1 (ORIG): read it with the Read tool from ${ROOT}/data/md/${id}.md (use its title + abstract body).
TEXT 2 (RESKIN): ${rw[i] ? rw[i].reskin : ''}
TEXT 3 (MATH): ${rw[i] ? rw[i].math : ''}

Return {id:"${id}", s_orig:<facet block for TEXT 1>, s_reskin:<facet block for TEXT 2>, s_math:<facet block for TEXT 3>}.`, { label:`sk:${id}`, phase:'Distill', model:'haiku', schema:SK_SCHEMA })))

log(`perturbation done: ${sk.filter(Boolean).length}/${IDS.length} papers`)
return { rewrites: rw, skeletons: sk }
