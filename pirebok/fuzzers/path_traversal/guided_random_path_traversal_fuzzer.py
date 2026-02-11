from typing import Sequence

from pirebok.fuzzers.fuzzer_visitor import FuzzerVisitor
from pirebok.fuzzers.guided_fuzzer_mixin import GuidedFuzzerMixin
from pirebok.fuzzers.path_traversal_fuzzer import PathTraversalFuzzer
from pirebok.transformers import Transformer


class GuidedRandomPathTraversalFuzzer(GuidedFuzzerMixin, PathTraversalFuzzer):
    _target_class = "path-traversal"

    def __init__(self, transformers: Sequence[Transformer]) -> None:
        super().__init__(transformers)
        self.threshold: float
        self.max_rounds: int = 100
        self.round_size: int = 20
        self.timeout: int = 0

    def accept(self, visitor: FuzzerVisitor) -> None:
        visitor.visit_path_traversal(self)
