# List + hash set for O(1) membership, still O(n) removal from the list — Time: insert O(1), remove O(n), getRandom O(1)
import random


class RandomizedSet:
    def __init__(self):
        self.values = []
        self.present = set()

    def insert(self, val: int) -> bool:
        if val in self.present:
            return False
        self.present.add(val)
        self.values.append(val)
        return True

    def remove(self, val: int) -> bool:
        if val not in self.present:
            return False
        self.present.remove(val)
        self.values.remove(val)  # still O(n): locate + shift
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
