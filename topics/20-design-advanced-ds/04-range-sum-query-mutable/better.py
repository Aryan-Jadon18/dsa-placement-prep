# Prefix sum array: O(1) range sum but O(n) rebuild on every update — Time: update O(n), sumRange O(1), Space: O(n)
from typing import List


class NumArray:
    def __init__(self, nums: List[int]):
        self.nums = nums[:]
        self.prefix = self._build_prefix()

    def _build_prefix(self) -> List[int]:
        n = len(self.nums)
        prefix = [0] * (n + 1)
        for i in range(n):
            prefix[i + 1] = prefix[i] + self.nums[i]
        return prefix

    def update(self, index: int, val: int) -> None:
        self.nums[index] = val
        self.prefix = self._build_prefix()  # O(n) rebuild from scratch

    def sumRange(self, left: int, right: int) -> int:
        return self.prefix[right + 1] - self.prefix[left]


if __name__ == "__main__":
    na = NumArray([1, 3, 5])
    print("Expected: 9, Got:", na.sumRange(0, 2))
    na.update(1, 2)
    print("Expected: 8, Got:", na.sumRange(0, 2))
