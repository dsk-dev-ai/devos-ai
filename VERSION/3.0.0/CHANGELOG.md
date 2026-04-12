# DevOS AI v3.0.0

## Highlights
- New `core/v3` architecture for advanced context construction.
- Direct replacement of the previous engine internals with strongly typed v3 builders.
- Explain command now supports:
  - `--max-files`
  - `--max-chars`
  - `--include-tests`
  - `--json`

## Technical Notes
- Legacy `core/engine.py` functions are kept as compatibility wrappers and now route to v3 internals.
- File scoring has been upgraded to keyword + file-type weighting.
- Prompt output now includes risks and gaps for practical code review.
