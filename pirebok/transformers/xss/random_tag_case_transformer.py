import random
import re

from pirebok.transformers.xss_transformer import XssTransformer


class RandomTagCaseTransformer(XssTransformer):
    def _randomize_case(self, tag: str) -> str:
        return "".join(c.swapcase() if random.random() > 0.5 else c for c in tag)

    def transform(self, payload: str) -> str:
        def replace_tag(m: re.Match) -> str:
            new_tag = self._randomize_case(m.group(2))
            return f"<{m.group(1)}{new_tag}"

        result = re.sub(r"<(/?)([a-zA-Z]+)", replace_tag, payload)
        if result == payload:
            result = re.sub(
                r"<(/?)([a-zA-Z]+)",
                lambda m: f"<{m.group(1)}{m.group(2).swapcase()}",
                payload,
            )
        return result
