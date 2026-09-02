# Plain recursion — Time: O(2^n), Space: O(n)
from typing import List


class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)

        def minCost(i: int) -> int:
            if i >= n:
                return 0
            return cost[i] + min(minCost(i + 1), minCost(i + 2))

        return min(minCost(0), minCost(1))


if __name__ == "__main__":
    sol = Solution()
    print("expected 15, got", sol.minCostClimbingStairs([10, 15, 20]))
    print("expected 6, got", sol.minCostClimbingStairs([1, 100, 1, 1, 1, 100, 1, 1, 100, 1]))
    print("expected 0, got", sol.minCostClimbingStairs([0, 0, 0, 1]))
