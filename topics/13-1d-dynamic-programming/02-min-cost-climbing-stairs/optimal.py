# Bottom-up tabulation, O(1) space — Time: O(n), Space: O(1)
from typing import List


class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        # dp[i] = min cost to arrive at step i; dp[0] = dp[1] = 0 (free start)
        prev2, prev1 = 0, 0
        for i in range(2, n + 1):
            prev2, prev1 = prev1, min(prev1 + cost[i - 1], prev2 + cost[i - 2])
        return prev1


if __name__ == "__main__":
    sol = Solution()
    print("expected 15, got", sol.minCostClimbingStairs([10, 15, 20]))
    print("expected 6, got", sol.minCostClimbingStairs([1, 100, 1, 1, 1, 100, 1, 1, 100, 1]))
    print("expected 0, got", sol.minCostClimbingStairs([0, 0, 0, 1]))
