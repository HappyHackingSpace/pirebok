import random
import time
from typing import Sequence

from pirebok.fuzzers.fuzzer_visitor import FuzzerVisitor
from pirebok.fuzzers.payload_pool import PayloadPool
from pirebok.fuzzers.sql_fuzzer import SqlFuzzer
from pirebok.transformers import Transformer


class GuidedRandomSqlFuzzer(SqlFuzzer):
    def __init__(self, transformers: Sequence[Transformer]) -> None:
        super().__init__(transformers)
        self.threshold: float
        self.max_rounds: int = 100
        self.round_size: int = 20
        self.timeout: int = 0

    def _mutation_round(self, payload: str, round_size: int) -> set[str]:
        return {random.choice(self.transformers).transform(payload) for _ in range(round_size)}

    def fuzz(self, payload: str) -> str:
        from metamaska.metamaska import Metamaska

        metamask = Metamaska()
        pool = PayloadPool()

        cls, proba = metamask.form(payload, True)
        confidence = proba if cls == "sqli" else 0.0
        pool.push(confidence, payload)

        best_confidence = confidence
        best_payload = payload

        deadline = (time.monotonic() + self.timeout) if self.timeout > 0 else 0.0

        for _ in range(self.max_rounds):
            if deadline and time.monotonic() >= deadline:
                break
            if best_confidence < self.threshold:
                break
            if not pool:
                break

            candidate_confidence, candidate = pool.pop()
            mutations = self._mutation_round(candidate, self.round_size)

            for mutated in mutations:
                cls, proba = metamask.form(mutated, True)
                mutation_confidence = proba if cls == "sqli" else 0.0
                pool.push(mutation_confidence, mutated)

                if mutation_confidence < best_confidence:
                    best_confidence = mutation_confidence
                    best_payload = mutated

            pool.push(candidate_confidence, candidate)

        return best_payload

    def accept(self, visitor: FuzzerVisitor) -> None:
        visitor.visit_sql(self)
