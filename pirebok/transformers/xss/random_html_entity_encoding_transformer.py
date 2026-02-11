import random

from pirebok.transformers.utils import filter_candidates, replace_random
from pirebok.transformers.xss_transformer import XssTransformer


class RandomHtmlEntityEncodingTransformer(XssTransformer):
    def __init__(self) -> None:
        self.symbols = {
            "<": ["&#60;", "&#x3c;", "&lt;"],
            ">": ["&#62;", "&#x3e;", "&gt;"],
            "'": ["&#39;", "&#x27;", "&apos;"],
            '"': ["&#34;", "&#x22;", "&quot;"],
            "/": ["&#47;", "&#x2f;"],
        }

    def transform(self, payload: str) -> str:
        candidates = filter_candidates(self.symbols, payload)
        if not candidates:
            return payload

        target = random.choice(candidates)
        replacement = random.choice(self.symbols[target])
        return replace_random(payload, target, replacement)
