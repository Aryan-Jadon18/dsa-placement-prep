# Bottom-up tabulation (unbounded knapsack) — Time: O(amount * coins), Space: O(amount)
from typing import List

INF = float("inf")


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [INF] * (amount + 1)
        dp[0] = 0
        for i in range(1, amount + 1):
            for c in coins:
                if c <= i:
                    dp[i] = min(dp[i], dp[i - c] + 1)
        return dp[amount] if dp[amount] != INF else -1


if __name__ == "__main__":
    sol = Solution()
    print("expected 3, got", sol.coinChange([1, 2, 5], 11))
    print("expected -1, got", sol.coinChange([2], 3))
    print("expected 0, got", sol.coinChange([1], 0))
