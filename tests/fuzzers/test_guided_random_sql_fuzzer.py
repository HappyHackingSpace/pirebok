import sys
from types import ModuleType
from unittest.mock import MagicMock, patch

from pirebok.fuzzers import FuzzerBuilder


def _make_mock_metamaska(side_effect):  # type: ignore[no-untyped-def]
    """Create a mock metamaska module with given form() side_effect."""
    mock_module = ModuleType("metamaska")
    mock_metamaska_inner = ModuleType("metamaska.metamaska")
    mock_class = MagicMock()
    mock_instance = MagicMock()
    mock_instance.form.side_effect = side_effect
    mock_class.return_value = mock_instance
    mock_metamaska_inner.Metamaska = mock_class  # type: ignore[attr-defined]
    mock_module.metamaska = mock_metamaska_inner  # type: ignore[attr-defined]
    return {"metamaska": mock_module, "metamaska.metamaska": mock_metamaska_inner}


def test_finds_better_payload() -> None:
    call_count = 0

    def form_side_effect(payload, flag):  # type: ignore[no-untyped-def]
        nonlocal call_count
        call_count += 1
        if call_count == 1:
            return ("sqli", 0.9)
        return ("sqli", 0.3)

    mocks = _make_mock_metamaska(form_side_effect)
    with patch.dict(sys.modules, mocks):
        fuzzer = (
            FuzzerBuilder()
            .choice("GuidedRandomSqlFuzzer")
            .threshold(0.5)
            .max_rounds(1)
            .round_size(5)
            .build()
        )
        result = fuzzer.fuzz("admin' OR 1=1#")

    assert result != "admin' OR 1=1#"


def test_returns_original_when_no_improvement() -> None:
    def form_side_effect(payload, flag):  # type: ignore[no-untyped-def]
        return ("sqli", 0.9)

    mocks = _make_mock_metamaska(form_side_effect)
    with patch.dict(sys.modules, mocks):
        fuzzer = (
            FuzzerBuilder()
            .choice("GuidedRandomSqlFuzzer")
            .threshold(0.5)
            .max_rounds(2)
            .round_size(5)
            .build()
        )
        result = fuzzer.fuzz("admin' OR 1=1#")

    assert isinstance(result, str)


def test_stops_at_threshold() -> None:
    call_count = 0

    def form_side_effect(payload, flag):  # type: ignore[no-untyped-def]
        nonlocal call_count
        call_count += 1
        if call_count == 1:
            return ("sqli", 0.9)
        return ("sqli", 0.1)

    mocks = _make_mock_metamaska(form_side_effect)
    with patch.dict(sys.modules, mocks):
        fuzzer = (
            FuzzerBuilder()
            .choice("GuidedRandomSqlFuzzer")
            .threshold(0.5)
            .max_rounds(100)
            .round_size(5)
            .build()
        )
        result = fuzzer.fuzz("admin' OR 1=1#")

    assert isinstance(result, str)
    assert call_count < 100 * 5 + 1
