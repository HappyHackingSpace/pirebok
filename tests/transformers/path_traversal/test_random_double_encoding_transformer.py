import pytest

from pirebok.transformers import RandomDoubleEncodingTransformer, Transformer


@pytest.fixture
def transformer() -> Transformer:
    return RandomDoubleEncodingTransformer()


def test_mutation(transformer: Transformer) -> None:
    payload = "../../etc/passwd"

    result = transformer.transform(payload)

    assert result != payload
    assert "%25" in result
