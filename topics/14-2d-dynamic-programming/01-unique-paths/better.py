# Top-down memoization — Time: O(m*n), Space: O(m*n)
from functools import lru_cache


class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        @lru_cache(maxsize=None)
        def walk(row: int, col: int) -> int:
            if row >= m or col >= n:
                return 0
            if row == m - 1 and col == n - 1:
                return 1
            return walk(row + 1, col) + walk(row, col + 1)

        result = walk(0, 0)
        walk.cache_clear()  # avoid cache bleeding across separate calls in this demo
        return result


if __name__ == "__main__":
    sol = Solution()
    print("expected 28, got", sol.uniquePaths(3, 7))
    print("expected 3, got", sol.uniquePaths(3, 2))
    print("expected 1, got", sol.uniquePaths(1, 1))
