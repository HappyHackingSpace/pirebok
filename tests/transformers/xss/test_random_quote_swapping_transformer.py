import pytest

from pirebok.transformers import RandomQuoteSwappingTransformer, Transformer


@pytest.fixture
def transformer() -> Transformer:
    return RandomQuoteSwappingTransformer()


def test_mutation(transformer: Transformer) -> None:
    payload = '<img src="x" onerror="alert(1)">'

    result = transformer.transform(payload)

    assert result != payload


def test_no_quotes_unchanged(transformer: Transformer) -> None:
    payload = "<script>alert(1)</script>"

    result = transformer.transform(payload)

    assert result == payload
