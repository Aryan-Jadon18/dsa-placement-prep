# Top-down memoization on (i, j) — Time: O(m*n), Space: O(m*n)
from functools import lru_cache


class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m, n = len(word1), len(word2)

        @lru_cache(maxsize=None)
        def dfs(i: int, j: int) -> int:
            if i == m:
                return n - j
            if j == n:
                return m - i
            if word1[i] == word2[j]:
                return dfs(i + 1, j + 1)
            replace = dfs(i + 1, j + 1)
            delete = dfs(i + 1, j)
            insert = dfs(i, j + 1)
            return 1 + min(replace, delete, insert)

        result = dfs(0, 0)
        dfs.cache_clear()
        return result


if __name__ == "__main__":
    sol = Solution()
    print("expected 3, got", sol.minDistance("horse", "ros"))
    print("expected 5, got", sol.minDistance("intention", "execution"))
    print("expected 3, got", sol.minDistance("", "abc"))
