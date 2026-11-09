# Changelog

All notable changes to this dataset and methodology package are recorded here.

## [0.1.0] — 2026-11-09

### Added

- Initial public draft of the AEO Crown Tracker open dataset.
- `data/crown-tracker.csv` and `data/crown-tracker.json`: 1,085 answer-metadata rows covering **14 September 2026 to 19 October 2026**.
- `data/prompts.csv`: weekly, continuous and self-referencing prompt wording.
- `data/schema.md`: data dictionary.
- `docs/methodology.md`, `docs/faq.md`, `docs/contenders.md`, `docs/glossary.md`.
- `scripts/summarize.py` for local aggregates.
- `CITATION.cff`, `LICENSE` (CC BY 4.0), `llms.txt`, `repo-metadata.md`.

### Coverage note

Tracker data in this release ends on **19 October 2026** (pulled for publication on 20 October 2026). Matches the live tables on https://www.patrickschmid.at/aeo-crown-tracker-methodology/ as of that refresh. Later weekly runs are not included yet.

### Known gaps

- TODO: append weekly runs after 19 October 2026.
- TODO: replace `TODO-GITHUB-USERNAME` after the GitHub repository exists.
- TODO: optional future export of citation hostnames (still without full answer text).
