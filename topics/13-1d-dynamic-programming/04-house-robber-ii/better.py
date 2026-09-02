# Top-down recursion + memoization on two linear sub-cases — Time: O(n), Space: O(n)
from functools import lru_cache
from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]

        def linearRob(arr: List[int]) -> int:
            @lru_cache(maxsize=None)
            def helper(i: int) -> int:
                if i >= len(arr):
                    return 0
                return max(arr[i] + helper(i + 2), helper(i + 1))

            result = helper(0)
            helper.cache_clear()
            return result

        return max(linearRob(nums[:-1]), linearRob(nums[1:]))


if __name__ == "__main__":
    sol = Solution()
    print("expected 3, got", sol.rob([2, 3, 2]))
    print("expected 4, got", sol.rob([1, 2, 3, 1]))
    print("expected 3, got", sol.rob([1, 2, 3]))
