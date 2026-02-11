import pytest

from pirebok.transformers import RandomWhitespaceAlternativeTransformer, Transformer


@pytest.fixture
def transformer() -> Transformer:
    return RandomWhitespaceAlternativeTransformer()


def test_mutation(transformer: Transformer) -> None:
    payload = "; cat /etc/passwd"

    result = transformer.transform(payload)

    assert result != payload


def test_no_space_unchanged(transformer: Transformer) -> None:
    payload = ";cat"

    result = transformer.transform(payload)

    assert result == payload
