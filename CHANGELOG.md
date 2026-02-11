# Changelog

## [0.2.0] - 2022-10-06
### Added
- Add threshold for the guided fuzzers

## [0.1.0] - 2022-10-04
### Added
- Initial release on PyPI.
- Random space substitution transformer
- Random case swapping transformer
- Random comment rewriting transformer
- Random comment removing transformer
- Random number encoding transformer
- Random keyword swapping transformer
- Random logical invariant appender transformer
- Random tautology swapping transformer
- Random generic fuzzer
- Random sql fuzzer
- Guided random sql fuzzer
- Add CLI support


## [Unreleased]
### Added
- Iterative evolutionary search for `GuidedRandomSqlFuzzer`
- `PayloadPool` — priority queue for ranked payloads with deduplication
- `RandomCommentInjectionTransformer` — inject `/**/` at random token boundaries
- `--max-rounds`, `--round-size`, `--timeout` CLI options and builder methods
