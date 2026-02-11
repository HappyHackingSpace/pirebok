import pytest

from pirebok.transformers import RandomSeparatorSwappingTransformer, Transformer


@pytest.fixture
def transformer() -> Transformer:
    return RandomSeparatorSwappingTransformer()


def test_mutation(transformer: Transformer) -> None:
    payload = "; cat /etc/passwd"

    result = transformer.transform(payload)

    assert result != payload


def test_no_separator_unchanged(transformer: Transformer) -> None:
    payload = "cat /etc/passwd"

    result = transformer.transform(payload)

    assert result == payload
