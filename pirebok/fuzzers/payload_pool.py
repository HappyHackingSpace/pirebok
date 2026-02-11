import heapq


class PayloadPool:
    def __init__(self) -> None:
        self._heap: list[tuple[float, str]] = []
        self._seen: set[str] = set()

    def push(self, confidence: float, payload: str) -> None:
        if payload in self._seen:
            return
        self._seen.add(payload)
        heapq.heappush(self._heap, (confidence, payload))

    def pop(self) -> tuple[float, str]:
        return heapq.heappop(self._heap)

    def peek(self) -> tuple[float, str]:
        return self._heap[0]

    def __len__(self) -> int:
        return len(self._heap)

    def __bool__(self) -> bool:
        return len(self._heap) > 0
