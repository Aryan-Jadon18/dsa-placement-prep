# Top-down recursion + memoization — Time: O(n), Space: O(n)
from functools import lru_cache


class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)

        @lru_cache(maxsize=None)
        def ways(i: int) -> int:
            if i == n:
                return 1
            if s[i] == '0':
                return 0
            total = ways(i + 1)
            if i + 1 < n and 10 <= int(s[i:i + 2]) <= 26:
                total += ways(i + 2)
            return total

        result = ways(0)
        ways.cache_clear()
        return result


if __name__ == "__main__":
    sol = Solution()
    print("expected 2, got", sol.numDecodings("12"))
    print("expected 3, got", sol.numDecodings("226"))
    print("expected 0, got", sol.numDecodings("06"))
