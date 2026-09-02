# Top-down memoization on (day, holding) — Time: O(n), Space: O(n)
from functools import lru_cache


class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        n = len(prices)

        @lru_cache(maxsize=None)
        def dfs(day: int, holding: bool) -> int:
            if day >= n:
                return 0
            skip = dfs(day + 1, holding)
            if holding:
                act = prices[day] + dfs(day + 2, False)
            else:
                act = -prices[day] + dfs(day + 1, True)
            return max(skip, act)

        result = dfs(0, False)
        dfs.cache_clear()
        return result


if __name__ == "__main__":
    sol = Solution()
    print("expected 3, got", sol.maxProfit([1, 2, 3, 0, 2]))
    print("expected 0, got", sol.maxProfit([1]))
    print("expected 3, got", sol.maxProfit([1, 4, 2]))
