import random

from pirebok.transformers.utils import replace_random
from pirebok.transformers.xss_transformer import XssTransformer


class RandomQuoteSwappingTransformer(XssTransformer):
    def transform(self, payload: str) -> str:
        candidates = []
        if '"' in payload:
            candidates.append('"')
        if "'" in payload:
            candidates.append("'")

        if not candidates:
            return payload

        target = random.choice(candidates)
        replacement = "'" if target == '"' else '"'
        return replace_random(payload, target, replacement)
