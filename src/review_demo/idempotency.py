class IdempotencyStore:
    def __init__(self):
        self._processed: set[str] = set()

    def was_processed(self, key: str) -> bool:
        return key in self._processed

    def mark_processed(self, key: str) -> None:
        self._processed.add(key)

    def clear(self, key: str) -> None:
        self._processed.discard(key)

