# Fenwick Tree (Binary Indexed Tree) — Time: update O(log n), sumRange O(log n), Space: O(n)
from typing import List


class NumArray:
    def __init__(self, nums: List[int]):
        self.n = len(nums)
        self.nums = [0] * self.n  # tracks current values, needed to compute deltas on update
        self.tree = [0] * (self.n + 1)  # 1-indexed Fenwick tree
        for i, val in enumerate(nums):
            self.update(i, val)

    def _add(self, index: int, delta: int) -> None:
        i = index + 1  # convert to 1-indexed
        while i <= self.n:
            self.tree[i] += delta
            i += i & (-i)  # jump to next node that also covers this index

    def _prefix_sum(self, index: int) -> int:
        # sum of nums[0..index], 0-indexed inclusive
        i = index + 1  # convert to 1-indexed
        total = 0
        while i > 0:
            total += self.tree[i]
            i -= i & (-i)  # jump to the previous owning node
        return total

    def update(self, index: int, val: int) -> None:
        delta = val - self.nums[index]
        self.nums[index] = val
        self._add(index, delta)

    def sumRange(self, left: int, right: int) -> int:
        if left == 0:
            return self._prefix_sum(right)
        return self._prefix_sum(right) - self._prefix_sum(left - 1)


if __name__ == "__main__":
    na = NumArray([1, 3, 5])
    print("Expected: 9, Got:", na.sumRange(0, 2))
    na.update(1, 2)
    print("Expected: 8, Got:", na.sumRange(0, 2))
    print("Expected: 1, Got:", na.sumRange(0, 0))
    print("Expected: 5, Got:", na.sumRange(2, 2))
