# Grouped by key + binary search on a dedicated timestamps list — Time: set O(1), get O(log k), Space: O(n)
import bisect
from collections import defaultdict


class TimeMap:
    def __init__(self):
        self.timestamps = defaultdict(list)  # key -> [ts0, ts1, ...] strictly increasing
        self.values = defaultdict(list)      # key -> [val0, val1, ...] parallel to timestamps

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.timestamps[key].append(timestamp)
        self.values[key].append(value)

    def get(self, key: str, timestamp: int) -> str:
        ts_list = self.timestamps.get(key)
        if not ts_list:
            return ""

        idx = bisect.bisect_right(ts_list, timestamp)
        if idx == 0:
            return ""
        return self.values[key][idx - 1]


if __name__ == "__main__":
    tm = TimeMap()
    tm.set("foo", "bar", 1)
    print("Expected: bar, Got:", tm.get("foo", 1))
    print("Expected: bar, Got:", tm.get("foo", 3))
    tm.set("foo", "bar2", 4)
    print("Expected: bar2, Got:", tm.get("foo", 4))
    print("Expected: bar2, Got:", tm.get("foo", 5))
    print("Expected: (empty), Got:", repr(tm.get("foo", 0)))
