import random
import re

from pirebok.transformers.cmdi_transformer import CmdiTransformer


class RandomVariableExpansionTransformer(CmdiTransformer):
    _expansions = [
        "${x}",
        "${EMPTY}",
        "${z}",
        "$@",
    ]

    def transform(self, payload: str) -> str:
        words = list(re.finditer(r"[a-zA-Z]{2,}", payload))
        if not words:
            return payload

        match = random.choice(words)
        word = match.group()
        pos = random.randint(1, len(word) - 1)
        expansion = random.choice(self._expansions)
        new_word = word[:pos] + expansion + word[pos:]
        return payload[: match.start()] + new_word + payload[match.end() :]
