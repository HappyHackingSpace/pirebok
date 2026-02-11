# Usage

To use pirebok in a project

```python
from pirebok.fuzzers import FuzzerBuilder
fuzzer_builder = FuzzerBuilder()
fuzzer = fuzzer_builder.choice("RandomGenericFuzzer").build()
fuzzer.fuzz("<script> ")
```

For the guided fuzzer with evolutionary search parameters:

```python
from pirebok.fuzzers import FuzzerBuilder
fuzzer = (
    FuzzerBuilder()
    .choice("GuidedRandomSqlFuzzer")
    .threshold(0.5)
    .max_rounds(100)
    .round_size(20)
    .timeout(30)
    .build()
)
fuzzer.fuzz("admin' OR 1=1#")
```

### XSS fuzzing

```python
from pirebok.fuzzers import FuzzerBuilder
fuzzer = FuzzerBuilder().choice("RandomXssFuzzer").build()
fuzzer.fuzz("<script>alert(1)</script>")
```

### Command injection fuzzing

```python
from pirebok.fuzzers import FuzzerBuilder
fuzzer = FuzzerBuilder().choice("RandomCmdiFuzzer").build()
fuzzer.fuzz("; cat /etc/passwd")
```

### Path traversal fuzzing

```python
from pirebok.fuzzers import FuzzerBuilder
fuzzer = FuzzerBuilder().choice("RandomPathTraversalFuzzer").build()
fuzzer.fuzz("../../etc/passwd")
```

To use from CLI

```
pirebok --help
Usage: pirebok [OPTIONS]

Options:
  -f, --fuzzer [guidedrandomcmdifuzzer|randomcmdifuzzer|randomgenericfuzzer|
                guidedrandompathtraversalfuzzer|randompathtraversalfuzzer|
                guidedrandomsqlfuzzer|randomsqlfuzzer|
                guidedrandomxssfuzzer|randomxssfuzzer]
                                  choose fuzzer  [required]
  -s, --steps INTEGER             Number of iteration  [default: 10]
  -t, --threshold FLOAT           Threshold for the guided fuzzers  [default: 0.5]
  --max-rounds INTEGER            Maximum mutation rounds for guided fuzzers  [default: 100]
  --round-size INTEGER            Mutations per round for guided fuzzers  [default: 20]
  --timeout INTEGER               Timeout in seconds, 0=unlimited  [default: 0]
  -p, --payload TEXT              Payload to fuzz  [required]
  -q, --silent                    Suppress banner
  --help                          Show this message and exit.
```

### Guided fuzzer options

| Option | Default | Description |
|--------|---------|-------------|
| `--max-rounds` | 100 | Maximum number of evolutionary mutation rounds per `fuzz()` call |
| `--round-size` | 20 | Number of mutations generated per round |
| `--timeout` | 0 | Timeout in seconds (0 = unlimited) |
| `-t, --threshold` | 0.5 | WAF confidence threshold — stop when confidence drops below this |
| `-s, --steps` | 10 | Number of independent `fuzz()` calls. For deep search use `--steps 1` with high `--max-rounds` |
