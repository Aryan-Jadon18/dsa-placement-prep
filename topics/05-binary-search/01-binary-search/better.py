# Recursive binary search — Time: O(log n), Space: O(log n) call stack
from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def helper(low: int, high: int) -> int:
            if low > high:
                return -1
            mid = (low + high) // 2
            if nums[mid] == target:
                return mid
            if nums[mid] < target:
                return helper(mid + 1, high)
            return helper(low, mid - 1)

        return helper(0, len(nums) - 1)


if __name__ == "__main__":
    sol = Solution()
    print("expected 4, got", sol.search([-1, 0, 3, 5, 9, 12], 9))
    print("expected -1, got", sol.search([-1, 0, 3, 5, 9, 12], 2))
    print("expected 0, got", sol.search([5], 5))
