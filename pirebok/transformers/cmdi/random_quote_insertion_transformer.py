import random
import re

from pirebok.transformers.cmdi_transformer import CmdiTransformer


class RandomQuoteInsertionTransformer(CmdiTransformer):
    _quote_pairs = ["''", '""']

    def transform(self, payload: str) -> str:
        words = list(re.finditer(r"[a-zA-Z]{2,}", payload))
        if not words:
            return payload

        match = random.choice(words)
        word = match.group()
        pos = random.randint(1, len(word) - 1)
        quotes = random.choice(self._quote_pairs)
        new_word = word[:pos] + quotes + word[pos:]
        return payload[: match.start()] + new_word + payload[match.end() :]
