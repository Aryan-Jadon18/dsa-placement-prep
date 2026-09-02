# Direct array, O(1) update, O(n) range sum — Time: update O(1), sumRange O(n), Space: O(n)
from typing import List


class NumArray:
    def __init__(self, nums: List[int]):
        self.nums = nums[:]

    def update(self, index: int, val: int) -> None:
        self.nums[index] = val

    def sumRange(self, left: int, right: int) -> int:
        return sum(self.nums[left:right + 1])


if __name__ == "__main__":
    na = NumArray([1, 3, 5])
    print("Expected: 9, Got:", na.sumRange(0, 2))
    na.update(1, 2)
    print("Expected: 8, Got:", na.sumRange(0, 2))
