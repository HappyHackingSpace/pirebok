import random

from pirebok.transformers.path_traversal_transformer import PathTraversalTransformer


class RandomNullByteAppenderTransformer(PathTraversalTransformer):
    _suffixes = [
        "%00",
        "%00.jpg",
        "%00.html",
        "%00.png",
        "\x00",
    ]

    def transform(self, payload: str) -> str:
        suffix = random.choice(self._suffixes)
        return payload + suffix
