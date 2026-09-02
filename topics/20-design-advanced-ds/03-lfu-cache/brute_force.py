# Single dict, scan all entries to find eviction victim — Time: O(1) hit / O(n) on eviction, Space: O(n)
class LFUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.clock = 0
        self.cache = {}  # key -> [value, freq, last_used_time]

    def _touch(self, key: int) -> None:
        self.clock += 1
        entry = self.cache[key]
        entry[1] += 1
        entry[2] = self.clock

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        self._touch(key)
        return self.cache[key][0]

    def put(self, key: int, value: int) -> None:
        if self.capacity <= 0:
            return

        if key in self.cache:
            self.cache[key][0] = value
            self._touch(key)
            return

        if len(self.cache) >= self.capacity:
            victim = min(self.cache, key=lambda k: (self.cache[k][1], self.cache[k][2]))
            del self.cache[victim]

        self.clock += 1
        self.cache[key] = [value, 1, self.clock]


if __name__ == "__main__":
    lfu = LFUCache(2)
    lfu.put(1, 1)
    lfu.put(2, 2)
    print("Expected: 1, Got:", lfu.get(1))
    lfu.put(3, 3)  # evicts key 2 (freq 1)
    print("Expected: -1, Got:", lfu.get(2))
    print("Expected: 3, Got:", lfu.get(3))
    lfu.put(4, 4)  # keys 1 and 3 tied at freq 2; key 1 used less recently -> evicted
    print("Expected: -1, Got:", lfu.get(1))
    print("Expected: 3, Got:", lfu.get(3))
    print("Expected: 4, Got:", lfu.get(4))
