# List + value->index map, swap-with-last for O(1) removal — Time: insert/remove/getRandom O(1), Space: O(n)
import random


class RandomizedSet:
    def __init__(self):
        self.values = []
        self.index_of = {}  # value -> index in self.values

    def insert(self, val: int) -> bool:
        if val in self.index_of:
            return False
        self.index_of[val] = len(self.values)
        self.values.append(val)
        return True

    def remove(self, val: int) -> bool:
        if val not in self.index_of:
            return False
        idx = self.index_of[val]
        last_val = self.values[-1]

        self.values[idx] = last_val
        self.index_of[last_val] = idx

        self.values.pop()
        del self.index_of[val]
        return True

    def getRandom(self) -> int:
        return random.choice(self.values)


if __name__ == "__main__":
    rs = RandomizedSet()
    print("Expected: True, Got:", rs.insert(1))
    print("Expected: False, Got:", rs.remove(2))
    print("Expected: True, Got:", rs.insert(2))
    print("getRandom (1 or 2):", rs.getRandom())
    print("Expected: True, Got:", rs.remove(1))
    print("Expected: False, Got:", rs.insert(2))
    print("Expected: 2, Got:", rs.getRandom())
