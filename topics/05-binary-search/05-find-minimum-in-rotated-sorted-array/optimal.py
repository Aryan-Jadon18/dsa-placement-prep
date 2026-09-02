# Binary search comparing mid to high, no special cases — Time: O(log n), Space: O(1)
from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
        low, high = 0, len(nums) - 1
        while low < high:
            mid = (low + high) // 2
            if nums[mid] > nums[high]:
                low = mid + 1
            else:
                high = mid
        return nums[low]


if __name__ == "__main__":
    sol = Solution()
    print("expected 1, got", sol.findMin([3, 4, 5, 1, 2]))
    print("expected 0, got", sol.findMin([4, 5, 6, 7, 0, 1, 2]))
    print("expected 11, got", sol.findMin([11, 13, 15, 17]))
