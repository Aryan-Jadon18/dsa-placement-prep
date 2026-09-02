# Single-pass binary search, determine sorted half at each step — Time: O(log n), Space: O(1)
from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        low, high = 0, len(nums) - 1
        while low <= high:
            mid = (low + high) // 2
            if nums[mid] == target:
                return mid

            if nums[low] <= nums[mid]:  # left half [low..mid] is sorted
                if nums[low] <= target < nums[mid]:
                    high = mid - 1
                else:
                    low = mid + 1
            else:  # right half [mid..high] is sorted
                if nums[mid] < target <= nums[high]:
                    low = mid + 1
                else:
                    high = mid - 1
        return -1


if __name__ == "__main__":
    sol = Solution()
    print("expected 4, got", sol.search([4, 5, 6, 7, 0, 1, 2], 0))
    print("expected -1, got", sol.search([4, 5, 6, 7, 0, 1, 2], 3))
    print("expected -1, got", sol.search([1], 0))
