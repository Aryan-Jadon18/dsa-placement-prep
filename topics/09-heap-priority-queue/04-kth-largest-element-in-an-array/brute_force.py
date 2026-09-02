# Full sort descending — Time: O(n log n), Space: O(n)
from typing import List


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        return sorted(nums, reverse=True)[k - 1]


if __name__ == "__main__":
    sol = Solution()
    print("Expected: 5  Actual:", sol.findKthLargest([3, 2, 1, 5, 6, 4], 2))
    print("Expected: 4  Actual:", sol.findKthLargest([3, 2, 3, 1, 2, 4, 5, 5, 6], 4))
    print("Expected: 1  Actual:", sol.findKthLargest([1], 1))
