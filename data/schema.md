# Data dictionary for the AEO Crown Tracker export

This file defines every column in `data/crown-tracker.csv` and every field in each object under `rows` in `data/crown-tracker.json`. The export covers 14 September 2026 to 19 October 2026. Full AI answer texts are not included.

## Dataset metadata (JSON only)

| Field | Type | Meaning |
| --- | --- | --- |
| `dataset` | string | Fixed id: `aeo-crown-tracker`. |
| `title` | string | Human-readable dataset title. |
| `description` | string | What the file contains and what it excludes. |
| `coverage_start` | date (YYYY-MM-DD) | First run date in the export. |
| `coverage_end` | date (YYYY-MM-DD) | Last run date in the export (19 October 2026). |
| `pulled_for_publication` | date | Date the log was pulled for the public methodology page (20 October 2026). |
| `row_count` | integer | Number of answer rows (1,085). |
| `prompt_set_counts` | object | Counts by `prompt_set`. |
| `engine_counts` | object | Counts by `engine`. |
| `source` | string | Provenance note and public methodology URL. |
| `license` | string | `CC BY 4.0`. |
| `rows` | array | The answer rows. |

## Row fields (CSV and JSON)

| Field | Type | Meaning |
| --- | --- | --- |
| `id` | string | Stable public row id (`ctr_` + 12 hex chars). Not a Rankscale internal id. |
| `date` | date (YYYY-MM-DD) | Calendar date of the run in UTC date of `executed_at_utc`. |
| `executed_at_utc` | datetime (ISO-8601, Z) | Exact execution timestamp in UTC. |
| `prompt` | string | Exact prompt wording sent to the engine. |
| `prompt_set` | enum | `weekly`, `continuous`, or `self_referencing`. See below. |
| `engine` | enum | `ChatGPT`, `Google AI Mode`, or `Google AI Overview`. |
| `market` | string | Always `US` in this release. |
| `language` | string | Always `en` in this release. |
| `answer_shown` | boolean | `false` when Google returned no AI Overview for that run; otherwise `true`. |
| `no_ai_overview` | boolean | Same signal as above, spelled for filters. Only meaningful for Google AI Overview. |
| `names_detected` | string list | People matched in the answer text (case-insensitive patterns). CSV uses `|` separators. |
| `named_first` | string | Tracked name whose first match appears earliest in the answer text; empty if none. |
| `patrick_schmid_named` | boolean | `true` if `Patrick Schmid` is in `names_detected`. |
| `patrickschmid_at_cited` | boolean | `true` if any citation URL is on `patrickschmid.at`. |
| `citation_count` | integer | Number of citation URLs recorded for the answer. |

## Prompt sets

**weekly.** Eight question-style prompts, run every Monday on ChatGPT, Google AI Mode and Google AI Overview. First Monday in this export: 14 September 2026. Last: 19 October 2026. Total: 144 answers (8 × 3 × 6).

**continuous.** Google AI Overview only: `King of AEO` (hourly), `Who is the King of AEO?` (daily), and `who is currently considered the king of aeo` (daily). Total: 761 answers.

**self_referencing.** `patrick schmid king of aeo` and `why is patrick schmid the new king of aeo`, hourly on Google AI Overview from 14 to 19 September 2026, then paused. Total: 180 answers. Kept out of the headline weekly and continuous counts on the methodology page.

## Name matching (as used for this export)

Tracked names and patterns used when the log was scored:

| Canonical name | Match idea (case-insensitive) |
| --- | --- |
| Patrick Schmid | `patrick schmid` |
| James Dooley | `dooley` |
| Vithurs | `vithurs` |
| David Quaid | `quaid` |
| Julian Goldie | `goldie` |
| Stephane Morera | `morera` |
| Allan Oliveira | `oliveira` |
| Marc Moeller | `moeller` / `möller` |
| Jacky Chou | `jacky chou` / `chou` |
| Edward Sturm | `sturm` |
| Chris (Cairns IT Guy) | `cairns` |

A surname match can fire in another context; treat counts as transparent measurements, not a courtroom verdict.

## What is intentionally omitted

- Full answer texts (they stay in the private tracking log).
- Citation URL lists (only the count and the patrickschmid.at boolean are public here).
- Rankscale brand ids, search-term ids, API keys and account identifiers.
- Engines and markets outside ChatGPT, Google AI Mode and Google AI Overviews in the United States.

## Related file: `prompts.csv`

| Column | Meaning |
| --- | --- |
| `prompt` | Exact wording. |
| `prompt_set` | `weekly`, `continuous`, or `self_referencing`. |
| `engines` | Engines that run that prompt (`;`-separated). |
| `frequency` | How often it ran in the coverage window. |
| `market` | `US`. |
| `language` | `en`. |
| `status` | `active_in_coverage_window` or `paused`. |

## Note on a one-row boundary difference

The public methodology page (updated 20 October 2026) reports 15 continuous Google AI Overview runs with no overview shown. This row-level export flags 16 continuous rows with `no_ai_overview=true` (12 for `King of AEO`, 4 for `who is currently considered the king of aeo`). Headline set sizes still match the page: weekly 144, continuous 761, self-referencing 180, total 1,085. See `docs/methodology.md`.
