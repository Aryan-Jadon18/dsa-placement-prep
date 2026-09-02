# All pairs with running sum per start index — Time: O(n^2), Space: O(1)
from typing import List


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        n = len(nums)
        count = 0
        for i in range(n):
            running = 0
            for j in range(i, n):
                running += nums[j]
                if running == k:
                    count += 1
        return count


if __name__ == "__main__":
    sol = Solution()
    print("expected 2, got", sol.subarraySum([1, 1, 1], 2))
    print("expected 2, got", sol.subarraySum([1, 2, 3], 3))
    print("expected 3, got", sol.subarraySum([1, -1, 0], 0))
