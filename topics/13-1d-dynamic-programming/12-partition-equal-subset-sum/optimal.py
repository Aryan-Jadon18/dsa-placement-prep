# Bottom-up 0/1 knapsack tabulation, 1D rolling array — Time: O(n * target), Space: O(target)
from typing import List


class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2 != 0:
            return False
        target = total // 2

        dp = [False] * (target + 1)
        dp[0] = True
        for num in nums:
            # iterate high to low so each num is used at most once per pass (0/1 knapsack)
            for s in range(target, num - 1, -1):
                if dp[s - num]:
                    dp[s] = True
        return dp[target]


if __name__ == "__main__":
    sol = Solution()
    print("expected True, got", sol.canPartition([1, 5, 11, 5]))
    print("expected False, got", sol.canPartition([1, 2, 3, 5]))
    print("expected False, got", sol.canPartition([1, 2, 5]))
