# Top-down recursion + memoization — Time: O(n), Space: O(n)
from functools import lru_cache
from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)

        @lru_cache(maxsize=None)
        def helper(i: int) -> int:
            if i >= n:
                return 0
            return max(nums[i] + helper(i + 2), helper(i + 1))

        result = helper(0)
        helper.cache_clear()
        return result


if __name__ == "__main__":
    sol = Solution()
    print("expected 4, got", sol.rob([1, 2, 3, 1]))
    print("expected 12, got", sol.rob([2, 7, 9, 3, 1]))
    print("expected 5, got", sol.rob([5]))
