# Grouped by key, linear backward scan within one key's history — Time: set O(1), get O(k), Space: O(n)
from collections import defaultdict


class TimeMap:
    def __init__(self):
        self.store = defaultdict(list)  # key -> list of (timestamp, value), increasing ts

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.store[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        history = self.store.get(key)
        if not history:
            return ""
        for ts, val in reversed(history):
            if ts <= timestamp:
                return val
        return ""


if __name__ == "__main__":
    tm = TimeMap()
    tm.set("foo", "bar", 1)
    print("Expected: bar, Got:", tm.get("foo", 1))
    print("Expected: bar, Got:", tm.get("foo", 3))
    tm.set("foo", "bar2", 4)
    print("Expected: bar2, Got:", tm.get("foo", 4))
    print("Expected: bar2, Got:", tm.get("foo", 5))
    print("Expected: (empty), Got:", repr(tm.get("foo", 0)))
