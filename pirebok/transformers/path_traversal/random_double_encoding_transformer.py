import random

from pirebok.transformers.path_traversal_transformer import PathTraversalTransformer
from pirebok.transformers.utils import replace_random


class RandomDoubleEncodingTransformer(PathTraversalTransformer):
    _encodings = {
        "../": ["%252e%252e%252f", "%252e%252e/", "..%252f"],
        "..\\": ["%252e%252e%255c", "%252e%252e\\", "..%255c"],
        "%2e": ["%252e"],
        "%2f": ["%252f"],
        "%5c": ["%255c"],
    }

    def transform(self, payload: str) -> str:
        found = [k for k in self._encodings if k in payload]
        if not found:
            return payload

        target = random.choice(found)
        replacement = random.choice(self._encodings[target])
        return replace_random(payload, target, replacement)
