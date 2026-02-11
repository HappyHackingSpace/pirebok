import pytest

from pirebok.transformers import RandomTagCaseTransformer, Transformer


@pytest.fixture
def transformer() -> Transformer:
    return RandomTagCaseTransformer()


def test_mutation(transformer: Transformer) -> None:
    payload = "<script>alert(1)</script>"

    result = transformer.transform(payload)

    assert result.lower() == payload.lower()
    assert result != payload
