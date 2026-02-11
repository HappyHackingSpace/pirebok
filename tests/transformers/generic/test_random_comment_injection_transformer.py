import pytest

from pirebok.transformers import RandomCommentInjectionTransformer, Transformer


@pytest.fixture
def transformer() -> Transformer:
    return RandomCommentInjectionTransformer()


def test_injects_comment(transformer: Transformer) -> None:
    payload = "SELECT 1 FROM users"

    result = transformer.transform(payload)

    assert "/**/" in result
    assert result != payload


def test_no_space_payload_unchanged(transformer: Transformer) -> None:
    payload = "SELECT"

    result = transformer.transform(payload)

    assert result == payload
