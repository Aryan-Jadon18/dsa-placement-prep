# Plain list, linear search for membership/removal — Time: insert O(n), remove O(n), getRandom O(1)
import random


class RandomizedSet:
    def __init__(self):
        self.values = []

    def insert(self, val: int) -> bool:
        if val in self.values:  # O(n) scan
            return False
        self.values.append(val)
        return True

    def remove(self, val: int) -> bool:
        if val not in self.values:
            return False
        self.values.remove(val)  # O(n) search + shift
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
