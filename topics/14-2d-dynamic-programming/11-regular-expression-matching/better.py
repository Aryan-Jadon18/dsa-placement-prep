# Top-down memoization on (i, j) — Time: O(m*n), Space: O(m*n)
from functools import lru_cache


class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        m, n = len(s), len(p)

        @lru_cache(maxsize=None)
        def dfs(i: int, j: int) -> bool:
            if j == n:
                return i == m
            first_match = i < m and (p[j] == s[i] or p[j] == ".")
            if j + 1 < n and p[j + 1] == "*":
                return dfs(i, j + 2) or (first_match and dfs(i + 1, j))
            return first_match and dfs(i + 1, j + 1)

        result = dfs(0, 0)
        dfs.cache_clear()
        return result


if __name__ == "__main__":
    sol = Solution()
    print("expected True, got", sol.isMatch("aa", "a*"))
    print("expected True, got", sol.isMatch("ab", ".*"))
    print("expected False, got", sol.isMatch("mississippi", "mis*is*p*."))
