# Top-down memoization on (index, open_count) — Time: O(n^2), Space: O(n^2)
from functools import lru_cache


class Solution:
    def checkValidString(self, s: str) -> bool:
        n = len(s)

        @lru_cache(maxsize=None)
        def dfs(i: int, open_count: int) -> bool:
            if open_count < 0 or open_count > n - i:
                return False
            if i == n:
                return open_count == 0
            c = s[i]
            if c == "(":
                return dfs(i + 1, open_count + 1)
            if c == ")":
                return dfs(i + 1, open_count - 1)
            return dfs(i + 1, open_count + 1) or dfs(i + 1, open_count - 1) or dfs(i + 1, open_count)

        result = dfs(0, 0)
        dfs.cache_clear()
        return result


if __name__ == "__main__":
    sol = Solution()
    print("expected True, got", sol.checkValidString("(*)"))
    print("expected True, got", sol.checkValidString("(*))"))
    print("expected False, got", sol.checkValidString("(()"))
