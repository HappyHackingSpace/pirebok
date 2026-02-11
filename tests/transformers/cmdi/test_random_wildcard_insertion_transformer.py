import pytest

from pirebok.transformers import RandomWildcardInsertionTransformer, Transformer


@pytest.fixture
def transformer() -> Transformer:
    return RandomWildcardInsertionTransformer()


def test_mutation(transformer: Transformer) -> None:
    payload = "; cat /etc/passwd"

    result = transformer.transform(payload)

    assert result != payload
