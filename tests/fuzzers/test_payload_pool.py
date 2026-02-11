import pytest

from pirebok.fuzzers import PayloadPool


@pytest.fixture
def pool() -> PayloadPool:
    return PayloadPool()


def test_push_pop_ordering(pool: PayloadPool) -> None:
    pool.push(0.9, "payload_a")
    pool.push(0.3, "payload_b")
    pool.push(0.7, "payload_c")

    assert pool.pop() == (0.3, "payload_b")
    assert pool.pop() == (0.7, "payload_c")
    assert pool.pop() == (0.9, "payload_a")


def test_peek(pool: PayloadPool) -> None:
    pool.push(0.5, "first")
    pool.push(0.2, "second")

    assert pool.peek() == (0.2, "second")
    assert len(pool) == 2


def test_dedup(pool: PayloadPool) -> None:
    pool.push(0.5, "dup")
    pool.push(0.3, "dup")

    assert len(pool) == 1
    assert pool.pop() == (0.5, "dup")


def test_empty_pool(pool: PayloadPool) -> None:
    assert len(pool) == 0
    assert not pool

    with pytest.raises(IndexError):
        pool.pop()

    with pytest.raises(IndexError):
        pool.peek()


def test_bool(pool: PayloadPool) -> None:
    assert not pool
    pool.push(0.5, "item")
    assert pool
