# Binary search for first index below nums[0] — Time: O(log n), Space: O(1)
from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
        n = len(nums)
        if nums[0] <= nums[-1]:  # no effective rotation, already sorted
            return nums[0]

        low, high = 0, n - 1
        while low < high:
            mid = (low + high) // 2
            if nums[mid] < nums[0]:
                high = mid  # rotation point is at mid or earlier
            else:
                low = mid + 1  # still in the "still >= nums[0]" zone
        return nums[low]


if __name__ == "__main__":
    sol = Solution()
    print("expected 1, got", sol.findMin([3, 4, 5, 1, 2]))
    print("expected 0, got", sol.findMin([4, 5, 6, 7, 0, 1, 2]))
    print("expected 11, got", sol.findMin([11, 13, 15, 17]))
