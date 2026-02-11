import pytest

from pirebok.transformers import RandomUnicodeNormalizationTransformer, Transformer


@pytest.fixture
def transformer() -> Transformer:
    return RandomUnicodeNormalizationTransformer()


def test_mutation(transformer: Transformer) -> None:
    payload = "../../etc/passwd"

    result = transformer.transform(payload)

    assert result != payload
