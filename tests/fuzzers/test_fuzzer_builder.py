import pytest

from pirebok.fuzzers import FuzzerBuilder, RandomGenericFuzzer


@pytest.fixture
def builder() -> FuzzerBuilder:
    return FuzzerBuilder()


def test_creation(builder: FuzzerBuilder) -> None:
    fuzzer_name = "RandomGenericFuzzer"

    fuzzer = builder.choice(fuzzer_name).threshold(0.5).build()

    assert isinstance(fuzzer, RandomGenericFuzzer)


def test_max_rounds(builder: FuzzerBuilder) -> None:
    fuzzer = builder.choice("RandomGenericFuzzer").max_rounds(50).build()

    assert fuzzer.max_rounds == 50  # type: ignore


def test_round_size(builder: FuzzerBuilder) -> None:
    fuzzer = builder.choice("RandomGenericFuzzer").round_size(10).build()

    assert fuzzer.round_size == 10  # type: ignore


def test_timeout(builder: FuzzerBuilder) -> None:
    fuzzer = builder.choice("RandomGenericFuzzer").timeout(30).build()

    assert fuzzer.timeout == 30  # type: ignore
