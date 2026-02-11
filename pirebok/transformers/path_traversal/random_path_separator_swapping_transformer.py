import random

from pirebok.transformers.path_traversal_transformer import PathTraversalTransformer
from pirebok.transformers.utils import replace_random


class RandomPathSeparatorSwappingTransformer(PathTraversalTransformer):
    def transform(self, payload: str) -> str:
        candidates = []
        if "/" in payload:
            candidates.append("/")
        if "\\" in payload:
            candidates.append("\\")

        if not candidates:
            return payload

        target = random.choice(candidates)
        replacement = "\\" if target == "/" else "/"
        return replace_random(payload, target, replacement)
