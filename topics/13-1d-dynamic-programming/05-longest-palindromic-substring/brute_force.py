# Check every substring — Time: O(n^3), Space: O(1) extra
class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        best = ""

        def isPalindrome(sub: str) -> bool:
            return sub == sub[::-1]

        for i in range(n):
            for j in range(i, n):
                candidate = s[i:j + 1]
                if len(candidate) > len(best) and isPalindrome(candidate):
                    best = candidate
        return best


if __name__ == "__main__":
    sol = Solution()
    print("expected len 3 palindrome, got", sol.longestPalindrome("babad"))
    print("expected bb, got", sol.longestPalindrome("cbbd"))
    print("expected a, got", sol.longestPalindrome("a"))
