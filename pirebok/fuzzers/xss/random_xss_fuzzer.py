import random

from pirebok.fuzzers.fuzzer_visitor import FuzzerVisitor
from pirebok.fuzzers.xss_fuzzer import XssFuzzer


class RandomXssFuzzer(XssFuzzer):
    def fuzz(self, payload: str) -> str:
        return random.choice(self.transformers).transform(payload)

    def accept(self, visitor: FuzzerVisitor) -> None:
        visitor.visit_xss(self)
