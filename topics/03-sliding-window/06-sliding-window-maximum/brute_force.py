# Scan each window fully for its max — Time: O(n * k), Space: O(1) extra
from typing import List


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        result = []
        for i in range(n - k + 1):
            result.append(max(nums[i:i + k]))
        return result


if __name__ == "__main__":
    sol = Solution()
    print("expected [3,3,5,5,6,7], got", sol.maxSlidingWindow([1, 3, -1, -3, 5, 3, 6, 7], 3))
    print("expected [1], got", sol.maxSlidingWindow([1], 1))
    print("expected [11], got", sol.maxSlidingWindow([9, 11], 2))
