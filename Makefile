# Reproduction package: cross-domain method-twin computational fingerprints.
#
# The derived corpus (skeletons + licensed abstracts) is BUNDLED under data/; five
# non-redistributable abstracts are rebuilt by `make restricted-data` (one online,
# sha256-verified step), after which both tables reproduce offline with no model:
#
#   make setup       create .venv and install requirements (one time)
#   make reproduce   print the two tables and write reproduce_out/
#   make data        OPTIONAL: rebuild the full-text corpus from the link lists
#   make help        show this list
#
# PY points at the venv interpreter made by `make setup`. Override to reuse your
# own environment, e.g.  make reproduce PY=python3

PY ?= .venv/bin/python
PIP ?= .venv/bin/pip

.PHONY: help setup data reproduce restricted-data

help:
	@echo "The corpus is bundled except five non-redistributable abstracts (one online rebuild step);"
	@echo "after that, reproduce needs no model and no network."
	@echo "Targets:"
	@echo "  setup            create .venv and install requirements.txt (one time)"
	@echo "  restricted-data  rebuild the five non-redistributable abstracts (online; sha256-verified)"
	@echo "  reproduce        print the two tables and write reproduce_out/   <- the main one"
	@echo "  data             OPTIONAL: rebuild the full-text corpus from the link lists"
	@echo "  help             show this message"

restricted-data:
	$(PY) src/fetch_restricted.py

setup:
	python3 -m venv .venv
	$(PIP) install --upgrade pip
	$(PIP) install -r requirements.txt
	@echo "[setup] done. Just run: make reproduce  (no .env needed; skeletons are bundled)."

reproduce:
	$(PY) reproduce.py
	@echo ""
	@echo "######## FACETED OPERATOR (needs ML extras): per-distiller combined-AP / facet-only AP / clustering ARI ########"
	@for d in skeletons_faceted_haiku skeletons_v1_opus skeletons_faceted_qwen_v3; do \
		$(PY) src/facet_select.py --skdir data/$$d 2>/dev/null | grep -A4 "FACETED SUMMARY" || true; \
	done
	@echo ""
	@echo "######## CONSTRUCT VALIDITY: three-arm blind wild precision (top vs random vs single-facet collision) ########"
	$(PY) src/wild_three_arm_score.py
	@echo ""
	@echo "######## PERTURBATION: interventional structure-vs-surface 2x2 (fingerprint vs abstract) ########"
	$(PY) src/perturbation_score.py

# Score the construct-validity + perturbation results alone (offline, from the shipped LLM outputs under
# datasets/validity/). Regenerating those outputs needs a model: src/wild_three_arm.py builds the blind
# pairs, then an LLM annotates them; src/perturbation_wf.js rewrites + distills. The scoring is deterministic.
.PHONY: validity
validity:
	$(PY) src/wild_three_arm_score.py
	$(PY) src/perturbation_score.py

# OPTIONAL. The package already ships the derived skeletons + abstracts, so you do
# NOT need this to reproduce the tables. It rebuilds the FULL-TEXT corpus from the
# link lists (network needed; paywalled / non-arXiv rows skip cleanly), overwriting
# the bundled abstract-only Markdown with full text. Distillation is separate
# (see README, "Regenerate the fingerprints").
data:
	$(PY) src/build_dataset.py datasets/mode_a_seed_families.csv --out data
	$(PY) src/build_dataset.py datasets/mode_b_discovery.csv --out data
	@echo "[data] full-text corpus rebuilt under data/. Now run: make reproduce"
