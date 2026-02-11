import random

from pirebok.transformers.path_traversal_transformer import PathTraversalTransformer
from pirebok.transformers.utils import filter_candidates, replace_random


class RandomUnicodeNormalizationTransformer(PathTraversalTransformer):
    def __init__(self) -> None:
        self.symbols = {
            "/": ["%c0%af", "%e0%80%af", "%c0%2f"],
            ".": ["%c0%ae", "%e0%80%ae", "%c0%2e"],
            "\\": ["%c1%9c", "%c0%5c"],
        }

    def transform(self, payload: str) -> str:
        candidates = filter_candidates(self.symbols, payload)
        if not candidates:
            return payload

        target = random.choice(candidates)
        replacement = random.choice(self.symbols[target])
        return replace_random(payload, target, replacement)
