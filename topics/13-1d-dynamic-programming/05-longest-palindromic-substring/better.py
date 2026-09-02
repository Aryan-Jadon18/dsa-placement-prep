# Top-down recursion + memoization (interval DP) — Time: O(n^2), Space: O(n^2)
from functools import lru_cache


class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)

        @lru_cache(maxsize=None)
        def isPalindrome(i: int, j: int) -> bool:
            if i >= j:
                return True
            if s[i] != s[j]:
                return False
            return isPalindrome(i + 1, j - 1)

        best = (0, 0)
        for i in range(n):
            for j in range(i, n):
                if isPalindrome(i, j) and (j - i) > (best[1] - best[0]):
                    best = (i, j)

        isPalindrome.cache_clear()
        return s[best[0]:best[1] + 1] if n else ""


if __name__ == "__main__":
    sol = Solution()
    print("expected len 3 palindrome, got", sol.longestPalindrome("babad"))
    print("expected bb, got", sol.longestPalindrome("cbbd"))
    print("expected a, got", sol.longestPalindrome("a"))
