import random

from pirebok.fuzzers.cmdi_fuzzer import CmdiFuzzer
from pirebok.fuzzers.fuzzer_visitor import FuzzerVisitor


class RandomCmdiFuzzer(CmdiFuzzer):
    def fuzz(self, payload: str) -> str:
        return random.choice(self.transformers).transform(payload)

    def accept(self, visitor: FuzzerVisitor) -> None:
        visitor.visit_cmdi(self)
