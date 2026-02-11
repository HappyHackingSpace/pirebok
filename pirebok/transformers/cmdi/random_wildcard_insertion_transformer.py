import random
import re

from pirebok.transformers.cmdi_transformer import CmdiTransformer


class RandomWildcardInsertionTransformer(CmdiTransformer):
    _wildcards = ["?", "*", "[]"]

    def transform(self, payload: str) -> str:
        words = list(re.finditer(r"[a-zA-Z]{3,}", payload))
        if not words:
            return payload

        match = random.choice(words)
        word = match.group()
        pos = random.randint(1, len(word) - 1)
        wildcard = random.choice(self._wildcards)

        if wildcard == "[]":
            char = word[pos]
            new_word = word[:pos] + f"[{char}]" + word[pos + 1 :]
        elif wildcard == "?":
            new_word = word[:pos] + "?" + word[pos + 1 :]
        else:
            new_word = word[:pos] + "*" + word[pos + 1 :]

        return payload[: match.start()] + new_word + payload[match.end() :]
