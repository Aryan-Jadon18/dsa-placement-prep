# Top-down recursion + memoization (interval DP) — Time: O(n^2), Space: O(n^2)
from functools import lru_cache


class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)

        @lru_cache(maxsize=None)
        def isPalindrome(i: int, j: int) -> bool:
            if i >= j:
                return True
            if s[i] != s[j]:
                return False
            return isPalindrome(i + 1, j - 1)

        count = 0
        for i in range(n):
            for j in range(i, n):
                if isPalindrome(i, j):
                    count += 1

        isPalindrome.cache_clear()
        return count


if __name__ == "__main__":
    sol = Solution()
    print("expected 3, got", sol.countSubstrings("abc"))
    print("expected 6, got", sol.countSubstrings("aaa"))
    print("expected 4, got", sol.countSubstrings("aba"))
