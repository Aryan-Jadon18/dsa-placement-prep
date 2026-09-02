# Dict + separate order list, O(n) scans — Time: O(n) per op, Space: O(capacity)


class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.store = {}
        self.order = []  # order[0] = least recently used, order[-1] = most recently used

    def _touch(self, key: int) -> None:
        self.order.remove(key)  # O(n)
        self.order.append(key)

    def get(self, key: int) -> int:
        if key not in self.store:
            return -1
        self._touch(key)
        return self.store[key]

    def put(self, key: int, value: int) -> None:
        if key in self.store:
            self.store[key] = value
            self._touch(key)
            return
        if len(self.store) >= self.capacity:
            oldest = self.order.pop(0)
            del self.store[oldest]
        self.store[key] = value
        self.order.append(key)


if __name__ == "__main__":
    cache = LRUCache(2)
    cache.put(1, 1)
    cache.put(2, 2)
    print("Expected: 1  Actual:", cache.get(1))
    cache.put(3, 3)  # evicts key 2
    print("Expected: -1  Actual:", cache.get(2))
    cache.put(4, 4)  # evicts key 1
    print("Expected: -1  Actual:", cache.get(1))
    print("Expected: 3  Actual:", cache.get(3))
    print("Expected: 4  Actual:", cache.get(4))

    cache2 = LRUCache(1)
    cache2.put(1, 1)
    cache2.put(2, 2)
    print("Expected: -1  Actual:", cache2.get(1))
    print("Expected: 2  Actual:", cache2.get(2))
