import random
import re

from pirebok.transformers.utils import replace_random
from pirebok.transformers.xss_transformer import XssTransformer


class RandomEventHandlerSwappingTransformer(XssTransformer):
    _handlers = [
        "onerror",
        "onload",
        "onfocus",
        "onblur",
        "onmouseover",
        "onmouseout",
        "onclick",
        "oninput",
        "onchange",
        "onsubmit",
        "onkeyup",
        "onkeydown",
    ]

    def transform(self, payload: str) -> str:
        found = [h for h in self._handlers if re.search(re.escape(h), payload, re.IGNORECASE)]
        if not found:
            return payload

        target = random.choice(found)
        alternatives = [h for h in self._handlers if h.lower() != target.lower()]
        replacement = random.choice(alternatives)
        return replace_random(payload, target, replacement)
