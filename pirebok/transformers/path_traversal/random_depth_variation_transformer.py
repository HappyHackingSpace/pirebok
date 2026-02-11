import random
import re

from pirebok.transformers.path_traversal_transformer import PathTraversalTransformer


class RandomDepthVariationTransformer(PathTraversalTransformer):
    def transform(self, payload: str) -> str:
        pattern = r"(\.\./|\.\.\\"
        pattern += r")"
        matches = list(re.finditer(r"\.\.[\\/]", payload))

        if not matches:
            return payload

        if random.random() > 0.5:
            sep = "/" if "/" in payload else "\\"
            insert_pos = matches[0].start()
            return payload[:insert_pos] + f"..{sep}" + payload[insert_pos:]
        else:
            if len(matches) > 1:
                target = random.choice(matches)
                return payload[: target.start()] + payload[target.end() :]

        return payload
