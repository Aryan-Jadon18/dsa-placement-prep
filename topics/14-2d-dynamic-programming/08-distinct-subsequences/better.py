# Top-down memoization on (i, j) — Time: O(len(s)*len(t)), Space: O(len(s)*len(t))
from functools import lru_cache


class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        m, n = len(s), len(t)

        @lru_cache(maxsize=None)
        def dfs(i: int, j: int) -> int:
            if j == n:
                return 1
            if i == m:
                return 0
            ways = dfs(i + 1, j)
            if s[i] == t[j]:
                ways += dfs(i + 1, j + 1)
            return ways

        result = dfs(0, 0)
        dfs.cache_clear()
        return result


if __name__ == "__main__":
    sol = Solution()
    print("expected 3, got", sol.numDistinct("rabbbit", "rabbit"))
    print("expected 5, got", sol.numDistinct("babgbag", "bag"))
    print("expected 0, got", sol.numDistinct("abc", "abcd"))
