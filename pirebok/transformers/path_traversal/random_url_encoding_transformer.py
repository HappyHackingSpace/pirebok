import random

from pirebok.transformers.path_traversal_transformer import PathTraversalTransformer
from pirebok.transformers.utils import replace_random


class RandomUrlEncodingTransformer(PathTraversalTransformer):
    _encodings = {
        "../": ["..%2f", "%2e%2e/", "%2e%2e%2f", "..%2F", "%2e./"],
        "..\\": ["..%5c", "%2e%2e\\", "%2e%2e%5c", "..%5C"],
        "./": [".%2f", "%2e/", "%2e%2f"],
    }

    def transform(self, payload: str) -> str:
        found = [k for k in self._encodings if k in payload]
        if not found:
            return payload

        target = random.choice(found)
        replacement = random.choice(self._encodings[target])
        return replace_random(payload, target, replacement)
