# heapq.nlargest over the full history each call — Time: O(n log k) per add, Space: O(n)
import heapq
from typing import List


class KthLargest:
    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.nums = list(nums)

    def add(self, val: int) -> int:
        self.nums.append(val)
        return heapq.nlargest(self.k, self.nums)[-1]


if __name__ == "__main__":
    kl = KthLargest(3, [4, 5, 8, 2])
    print("Expected: 4  Actual:", kl.add(3))
    print("Expected: 5  Actual:", kl.add(5))
    print("Expected: 5  Actual:", kl.add(10))
    print("Expected: 8  Actual:", kl.add(9))

    kl2 = KthLargest(1, [])
    print("Expected: -3  Actual:", kl2.add(-3))
