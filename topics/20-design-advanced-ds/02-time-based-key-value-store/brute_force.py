# One flat list of all entries, linear scan + filter on every get — Time: set O(1), get O(n), Space: O(n)
class TimeMap:
    def __init__(self):
        self.entries = []  # list of (key, timestamp, value)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.entries.append((key, timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        best_ts = -1
        best_val = ""
        for k, ts, val in self.entries:
            if k == key and ts <= timestamp and ts > best_ts:
                best_ts = ts
                best_val = val
        return best_val


if __name__ == "__main__":
    tm = TimeMap()
    tm.set("foo", "bar", 1)
    print("Expected: bar, Got:", tm.get("foo", 1))
    print("Expected: bar, Got:", tm.get("foo", 3))
    tm.set("foo", "bar2", 4)
    print("Expected: bar2, Got:", tm.get("foo", 4))
    print("Expected: bar2, Got:", tm.get("foo", 5))
    print("Expected: (empty), Got:", repr(tm.get("foo", 0)))
