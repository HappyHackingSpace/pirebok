import random

from pirebok.transformers.cmdi_transformer import CmdiTransformer
from pirebok.transformers.utils import replace_random


class RandomWhitespaceAlternativeTransformer(CmdiTransformer):
    _alternatives = [
        "${IFS}",
        "$IFS",
        "\t",
        "{,}",
        "$IFS$9",
    ]

    def transform(self, payload: str) -> str:
        if " " not in payload:
            return payload

        replacement = random.choice(self._alternatives)
        return replace_random(payload, " ", replacement)
