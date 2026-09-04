# Models, prompt versions, and run dates (per arm)

Every LLM-touched artifact in this package, by arm. Provenance: the research-workspace run logs
(`qwen_v3.log`, `watchdog.log`), the distillation scripts, the workflow files, and the dated state
notes; entries marked "inferred" come from the code defaults of the period rather than a run log.
Hosted-model arms were run through dispatched agent sessions (no raw API access), so temperature is
the session default. The distillation prompt is the verbatim `DISTILL_PROMPT` in
`src/distill_faceted.py` (faceted v3, the shipped configuration); the v1 skeleton prompt is in
`src/distill_v1.py`; the perturbation prompts are in `src/perturbation_wf.js`; the blind
three-arm annotation prompt is described in `DATASET.md`.

| Arm | Artifact | Model identifier | Prompt | Run date |
|---|---|---|---|---|
| Distiller, ours (Haiku) | `data/skeletons_faceted_haiku/` | claude-haiku-4-5-20251001 | faceted v3 | 2026-06-26 (watchdog log: 497/497) |
| Distiller, comparison (Opus) | `data/skeletons_v1_opus/` | claude-opus-4-8 (inferred: the period's code default) | v1 skeleton prompt | 2026-06-25/26 (agent waves; complete by 06-27) |
| Distiller, comparison (local) | `data/skeletons_faceted_qwen_v3/` | qwen3:14b via ollama on a remote RTX 4070 Ti (`qwen_v3.log`: `[distill_faceted:ollama/qwen3:14b] ok=497 fail=0`) | faceted v3 | 2026-06-26 (overnight, ~7 h) |
| Keep-domain ablation | `data/skeletons_keepdomain_qwen/` | qwen3:14b (same run family) | faceted v3, keep-domain variant | 2026-06-26/27 |
| Wild annotator 1 (distiller model) | `datasets/validity/wild_3arm_annotations.json`, `Claude (blind annotation)` | claude-haiku-4-5-20251001 (the distiller arm; the other two are the non-distiller annotators) | blind three-arm annotation | 2026-06-29 |
| Wild annotator 2 | same, `claude-sonnet-4-6` | claude-sonnet-4-6 | same | 2026-06-29 |
| Wild annotator 3 | same, `claude-opus-cross-domain-strict` (run label) | claude-opus-4-8 (inferred), strict variant | same | 2026-06-29 |
| Perturbation rewriter | `datasets/validity/perturbation.json` (`reskin`, `math`) | Sonnet (agent alias `sonnet`; claude-sonnet-4-6 in this period), deliberately a different model from the distiller | `src/perturbation_wf.js` (Rewrite phase) | 2026-06-29 |
| Perturbation re-distiller | same (`s_orig`, `s_reskin`, `s_math`) | Haiku (agent alias `haiku`; claude-haiku-4-5-20251001) | `src/perturbation_wf.js` (Distill phase) | 2026-06-29 |

Note. `src/distill_faceted.py` still lists `qwen2.5:14b-instruct` as its ollama default; that
model was used only for an unshipped v1-prompt arm that timed out. Anyone regenerating the local
arm should pass `--model qwen3:14b`.
