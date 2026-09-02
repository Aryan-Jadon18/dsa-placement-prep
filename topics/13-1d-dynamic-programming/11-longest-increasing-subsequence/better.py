# Top-down recursion + memoization — Time: O(n^2), Space: O(n)
from functools import lru_cache
from typing import List


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)

        @lru_cache(maxsize=None)
        def lengthFrom(i: int) -> int:
            best = 1
            for j in range(i + 1, n):
                if nums[j] > nums[i]:
                    best = max(best, 1 + lengthFrom(j))
            return best

        result = max(lengthFrom(i) for i in range(n))
        lengthFrom.cache_clear()
        return result


if __name__ == "__main__":
    sol = Solution()
    print("expected 4, got", sol.lengthOfLIS([10, 9, 2, 5, 3, 7, 101, 18]))
    print("expected 4, got", sol.lengthOfLIS([0, 1, 0, 3, 2, 3]))
    print("expected 1, got", sol.lengthOfLIS([7, 7, 7, 7]))
