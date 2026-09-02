# Top-down recursion + memoization — Time: O(amount * coins), Space: O(amount)
from functools import lru_cache
from typing import List

INF = float("inf")


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        @lru_cache(maxsize=None)
        def minCoins(remaining: int) -> float:
            if remaining == 0:
                return 0
            if remaining < 0:
                return INF
            best = INF
            for c in coins:
                if c <= remaining:
                    best = min(best, 1 + minCoins(remaining - c))
            return best

        result = minCoins(amount)
        minCoins.cache_clear()
        return result if result != INF else -1


if __name__ == "__main__":
    sol = Solution()
    print("expected 3, got", sol.coinChange([1, 2, 5], 11))
    print("expected -1, got", sol.coinChange([2], 3))
    print("expected 0, got", sol.coinChange([1], 0))
