import pytest

from pirebok.transformers import RandomEventHandlerSwappingTransformer, Transformer


@pytest.fixture
def transformer() -> Transformer:
    return RandomEventHandlerSwappingTransformer()


def test_mutation(transformer: Transformer) -> None:
    payload = '<img src=x onerror=alert(1)>'

    result = transformer.transform(payload)

    assert result != payload
    assert "alert(1)" in result


def test_no_handler_unchanged(transformer: Transformer) -> None:
    payload = "<p>hello</p>"

    result = transformer.transform(payload)

    assert result == payload
