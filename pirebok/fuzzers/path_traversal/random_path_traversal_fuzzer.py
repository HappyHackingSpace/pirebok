import random

from pirebok.fuzzers.fuzzer_visitor import FuzzerVisitor
from pirebok.fuzzers.path_traversal_fuzzer import PathTraversalFuzzer


class RandomPathTraversalFuzzer(PathTraversalFuzzer):
    def fuzz(self, payload: str) -> str:
        return random.choice(self.transformers).transform(payload)

    def accept(self, visitor: FuzzerVisitor) -> None:
        visitor.visit_path_traversal(self)
