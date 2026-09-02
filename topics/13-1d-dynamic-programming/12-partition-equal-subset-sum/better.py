# Top-down recursion + memoization — Time: O(n * target), Space: O(n * target)
from functools import lru_cache
from typing import List


class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2 != 0:
            return False
        target = total // 2
        n = len(nums)

        @lru_cache(maxsize=None)
        def canReach(i: int, remaining: int) -> bool:
            if remaining == 0:
                return True
            if i == n or remaining < 0:
                return False
            return canReach(i + 1, remaining - nums[i]) or canReach(i + 1, remaining)

        result = canReach(0, target)
        canReach.cache_clear()
        return result


if __name__ == "__main__":
    sol = Solution()
    print("expected True, got", sol.canPartition([1, 5, 11, 5]))
    print("expected False, got", sol.canPartition([1, 2, 3, 5]))
    print("expected False, got", sol.canPartition([1, 2, 5]))
