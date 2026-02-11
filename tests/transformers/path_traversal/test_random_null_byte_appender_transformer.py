import pytest

from pirebok.transformers import RandomNullByteAppenderTransformer, Transformer


@pytest.fixture
def transformer() -> Transformer:
    return RandomNullByteAppenderTransformer()


def test_mutation(transformer: Transformer) -> None:
    payload = "../../etc/passwd"

    result = transformer.transform(payload)

    assert result != payload
    assert result.startswith(payload)
