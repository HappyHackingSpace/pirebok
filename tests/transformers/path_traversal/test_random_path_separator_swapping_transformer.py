import pytest

from pirebok.transformers import RandomPathSeparatorSwappingTransformer, Transformer


@pytest.fixture
def transformer() -> Transformer:
    return RandomPathSeparatorSwappingTransformer()


def test_mutation(transformer: Transformer) -> None:
    payload = "../../etc/passwd"

    result = transformer.transform(payload)

    assert result != payload
    assert "\\" in result
