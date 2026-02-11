import random

from pirebok.transformers.utils import replace_random
from pirebok.transformers.xss_transformer import XssTransformer


class RandomProtocolObfuscationTransformer(XssTransformer):
    _alternatives = [
        "java\tscript:",
        "java\nscript:",
        "java\rscript:",
        "java\x00script:",
        "jav\tascript:",
        "javas\tcript:",
    ]

    def transform(self, payload: str) -> str:
        lower = payload.lower()
        if "javascript:" not in lower:
            return payload

        idx = lower.index("javascript:")
        original = payload[idx : idx + len("javascript:")]
        replacement = random.choice(self._alternatives)
        return replace_random(payload, original, replacement)
