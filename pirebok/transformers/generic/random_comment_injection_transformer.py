import random
import re

from pirebok.transformers.generic_transformer import GenericTransformer


class RandomCommentInjectionTransformer(GenericTransformer):
    def transform(self, payload: str) -> str:
        spaces = list(re.finditer(r"\s+", payload))
        if not spaces:
            return payload
        match = random.choice(spaces)
        return payload[: match.start()] + "/**/" + payload[match.end() :]
