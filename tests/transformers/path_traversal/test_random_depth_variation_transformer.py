import pytest

from pirebok.transformers import RandomDepthVariationTransformer, Transformer


@pytest.fixture
def transformer() -> Transformer:
    return RandomDepthVariationTransformer()


def test_mutation(transformer: Transformer) -> None:
    payload = "../../etc/passwd"

    result = transformer.transform(payload)

    assert result != payload
