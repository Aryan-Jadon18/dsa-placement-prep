# OrderedDict for O(1) amortized move-to-end / pop-oldest — Time: O(1) amortized, Space: O(capacity)
from collections import OrderedDict


class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.store: OrderedDict[int, int] = OrderedDict()

    def get(self, key: int) -> int:
        if key not in self.store:
            return -1
        self.store.move_to_end(key)
        return self.store[key]

    def put(self, key: int, value: int) -> None:
        if key in self.store:
            self.store.move_to_end(key)
        self.store[key] = value
        if len(self.store) > self.capacity:
            self.store.popitem(last=False)  # evict least recently used


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
