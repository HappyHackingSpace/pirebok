import random

from pirebok.transformers.cmdi_transformer import CmdiTransformer
from pirebok.transformers.utils import filter_candidates, replace_random


class RandomSeparatorSwappingTransformer(CmdiTransformer):
    def __init__(self) -> None:
        self.symbols = {
            ";": ["|", "&&", "||", "\n", "&"],
            "|": [";", "&&", "||", "\n", "&"],
            "&&": [";", "|", "||", "\n"],
            "||": [";", "|", "&&", "\n"],
            "\n": [";", "|", "&&", "||"],
        }

    def transform(self, payload: str) -> str:
        candidates = filter_candidates(self.symbols, payload)
        if not candidates:
            return payload

        target = random.choice(candidates)
        replacement = random.choice(self.symbols[target])
        return replace_random(payload, target, replacement)
