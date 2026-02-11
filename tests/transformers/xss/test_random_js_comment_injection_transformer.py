import pytest

from pirebok.transformers import RandomJsCommentInjectionTransformer, Transformer


@pytest.fixture
def transformer() -> Transformer:
    return RandomJsCommentInjectionTransformer()


def test_mutation(transformer: Transformer) -> None:
    payload = "<script>alert(1)</script>"

    result = transformer.transform(payload)

    assert "/**/" in result
    assert result != payload


def test_no_parens_unchanged(transformer: Transformer) -> None:
    payload = "<b>hello</b>"

    result = transformer.transform(payload)

    assert result == payload
