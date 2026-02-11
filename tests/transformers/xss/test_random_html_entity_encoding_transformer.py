import pytest

from pirebok.transformers import RandomHtmlEntityEncodingTransformer, Transformer


@pytest.fixture
def transformer() -> Transformer:
    return RandomHtmlEntityEncodingTransformer()


def test_mutation(transformer: Transformer) -> None:
    payload = "<script>alert(1)</script>"

    result = transformer.transform(payload)

    assert result != payload
