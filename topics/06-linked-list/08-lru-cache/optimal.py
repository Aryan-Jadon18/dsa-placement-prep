# HashMap + custom doubly linked list with sentinels — Time: O(1) worst case, Space: O(capacity)


class DLLNode:
    def __init__(self, key=0, val=0):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None


class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}  # key -> DLLNode

        # sentinels: head.next = most recently used, tail.prev = least recently used
        self.head = DLLNode()
        self.tail = DLLNode()
        self.head.next = self.tail
        self.tail.prev = self.head

    def _remove(self, node: DLLNode) -> None:
        node.prev.next = node.next
        node.next.prev = node.prev

    def _insert_at_front(self, node: DLLNode) -> None:
        node.next = self.head.next
        node.prev = self.head
        self.head.next.prev = node
        self.head.next = node

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        node = self.cache[key]
        self._remove(node)
        self._insert_at_front(node)
        return node.val

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            node = self.cache[key]
            node.val = value
            self._remove(node)
            self._insert_at_front(node)
            return

        if len(self.cache) >= self.capacity:
            lru = self.tail.prev
            self._remove(lru)
            del self.cache[lru.key]

        node = DLLNode(key, value)
        self.cache[key] = node
        self._insert_at_front(node)


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
