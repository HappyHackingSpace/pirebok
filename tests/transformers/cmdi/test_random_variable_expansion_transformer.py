import pytest

from pirebok.transformers import RandomVariableExpansionTransformer, Transformer


@pytest.fixture
def transformer() -> Transformer:
    return RandomVariableExpansionTransformer()


def test_mutation(transformer: Transformer) -> None:
    payload = "; cat /etc/passwd"

    result = transformer.transform(payload)

    assert result != payload
    assert "${" in result or "$@" in result
