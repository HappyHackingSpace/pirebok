import random
import re

from pirebok.transformers.xss_transformer import XssTransformer


class RandomJsCommentInjectionTransformer(XssTransformer):
    def transform(self, payload: str) -> str:
        parens = list(re.finditer(r"(?<!\*)\(", payload))
        if not parens:
            return payload

        pos = random.choice(parens).start()
        return payload[:pos] + "/**/" + payload[pos:]
