# Top-down memoization on (coin_index, remaining) — Time: O(len(coins)*amount), Space: O(len(coins)*amount)
from functools import lru_cache


class Solution:
    def change(self, amount: int, coins: list[int]) -> int:
        n = len(coins)

        @lru_cache(maxsize=None)
        def ways(i: int, remaining: int) -> int:
            if remaining == 0:
                return 1
            if remaining < 0 or i == n:
                return 0
            skip = ways(i + 1, remaining)
            use = ways(i, remaining - coins[i])
            return skip + use

        result = ways(0, amount)
        ways.cache_clear()
        return result


if __name__ == "__main__":
    sol = Solution()
    print("expected 4, got", sol.change(5, [1, 2, 5]))
    print("expected 0, got", sol.change(3, [2]))
    print("expected 1, got", sol.change(0, [1, 2, 3]))
