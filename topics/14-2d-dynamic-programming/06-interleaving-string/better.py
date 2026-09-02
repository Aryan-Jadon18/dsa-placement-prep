# Top-down memoization on (i, j) — Time: O(m*n), Space: O(m*n)
from functools import lru_cache


class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        m, n = len(s1), len(s2)
        if m + n != len(s3):
            return False

        @lru_cache(maxsize=None)
        def dfs(i: int, j: int) -> bool:
            if i == m and j == n:
                return True
            k = i + j
            take_s1 = i < m and s1[i] == s3[k] and dfs(i + 1, j)
            take_s2 = j < n and s2[j] == s3[k] and dfs(i, j + 1)
            return take_s1 or take_s2

        result = dfs(0, 0)
        dfs.cache_clear()
        return result


if __name__ == "__main__":
    sol = Solution()
    print("expected True, got", sol.isInterleave("aab", "axy", "aaaxby"))
    print("expected False, got", sol.isInterleave("abc", "xyz", "abcxzy"))
    print("expected True, got", sol.isInterleave("", "abc", "abc"))
