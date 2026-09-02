# Frequency buckets as plain lists (O(bucket size) list.remove on every touch) — Time: O(b), Space: O(n)
from collections import defaultdict


class LFUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.min_freq = 0
        self.key_to_val = {}
        self.key_to_freq = {}
        self.freq_to_keys = defaultdict(list)  # freq -> [keys in use order], front = LRU

    def _bump(self, key: int) -> None:
        freq = self.key_to_freq[key]
        self.freq_to_keys[freq].remove(key)  # O(bucket size) shift
        if not self.freq_to_keys[freq] and freq == self.min_freq:
            self.min_freq += 1
        new_freq = freq + 1
        self.key_to_freq[key] = new_freq
        self.freq_to_keys[new_freq].append(key)

    def get(self, key: int) -> int:
        if key not in self.key_to_val:
            return -1
        self._bump(key)
        return self.key_to_val[key]

    def put(self, key: int, value: int) -> None:
        if self.capacity <= 0:
            return

        if key in self.key_to_val:
            self.key_to_val[key] = value
            self._bump(key)
            return

        if len(self.key_to_val) >= self.capacity:
            victim = self.freq_to_keys[self.min_freq].pop(0)  # O(bucket size) shift
            del self.key_to_val[victim]
            del self.key_to_freq[victim]

        self.key_to_val[key] = value
        self.key_to_freq[key] = 1
        self.freq_to_keys[1].append(key)
        self.min_freq = 1


if __name__ == "__main__":
    lfu = LFUCache(2)
    lfu.put(1, 1)
    lfu.put(2, 2)
    print("Expected: 1, Got:", lfu.get(1))
    lfu.put(3, 3)
    print("Expected: -1, Got:", lfu.get(2))
    print("Expected: 3, Got:", lfu.get(3))
    lfu.put(4, 4)
    print("Expected: -1, Got:", lfu.get(1))
    print("Expected: 3, Got:", lfu.get(3))
    print("Expected: 4, Got:", lfu.get(4))
