import pytest

from pirebok.transformers import RandomQuoteInsertionTransformer, Transformer


@pytest.fixture
def transformer() -> Transformer:
    return RandomQuoteInsertionTransformer()


def test_mutation(transformer: Transformer) -> None:
    payload = "; cat /etc/passwd"

    result = transformer.transform(payload)

    assert result != payload
    assert "''" in result or '""' in result
