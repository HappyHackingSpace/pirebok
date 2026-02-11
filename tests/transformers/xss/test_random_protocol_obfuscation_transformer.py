import pytest

from pirebok.transformers import RandomProtocolObfuscationTransformer, Transformer


@pytest.fixture
def transformer() -> Transformer:
    return RandomProtocolObfuscationTransformer()


def test_mutation(transformer: Transformer) -> None:
    payload = '<a href="javascript:alert(1)">'

    result = transformer.transform(payload)

    assert result != payload
    assert "javascript:" not in result


def test_no_protocol_unchanged(transformer: Transformer) -> None:
    payload = "<script>alert(1)</script>"

    result = transformer.transform(payload)

    assert result == payload
