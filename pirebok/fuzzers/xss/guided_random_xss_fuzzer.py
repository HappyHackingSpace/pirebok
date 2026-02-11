from typing import Sequence

from pirebok.fuzzers.fuzzer_visitor import FuzzerVisitor
from pirebok.fuzzers.guided_fuzzer_mixin import GuidedFuzzerMixin
from pirebok.fuzzers.xss_fuzzer import XssFuzzer
from pirebok.transformers import Transformer


class GuidedRandomXssFuzzer(GuidedFuzzerMixin, XssFuzzer):
    _target_class = "xss"

    def __init__(self, transformers: Sequence[Transformer]) -> None:
        super().__init__(transformers)
        self.threshold: float
        self.max_rounds: int = 100
        self.round_size: int = 20
        self.timeout: int = 0

    def accept(self, visitor: FuzzerVisitor) -> None:
        visitor.visit_xss(self)
