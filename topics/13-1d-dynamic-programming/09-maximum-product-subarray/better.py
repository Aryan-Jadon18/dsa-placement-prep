# Top-down recursion + memoization on max/min ending here — Time: O(n), Space: O(n)
from functools import lru_cache
from typing import List


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        n = len(nums)

        @lru_cache(maxsize=None)
        def maxEnd(i: int) -> int:
            if i == 0:
                return nums[0]
            return max(nums[i], nums[i] * maxEnd(i - 1), nums[i] * minEnd(i - 1))

        @lru_cache(maxsize=None)
        def minEnd(i: int) -> int:
            if i == 0:
                return nums[0]
            return min(nums[i], nums[i] * maxEnd(i - 1), nums[i] * minEnd(i - 1))

        result = max(maxEnd(i) for i in range(n))
        maxEnd.cache_clear()
        minEnd.cache_clear()
        return result


if __name__ == "__main__":
    sol = Solution()
    print("expected 6, got", sol.maxProduct([2, 3, -2, 4]))
    print("expected 0, got", sol.maxProduct([-2, 0, -1]))
    print("expected 24, got", sol.maxProduct([-2, 3, -4]))
