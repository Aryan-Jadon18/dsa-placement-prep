# Expand around center, O(1) extra space — Time: O(n^2), Space: O(1)
class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s:
            return ""

        def expand(left: int, right: int) -> tuple:
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            # after loop, s[left+1 .. right-1] is the widest palindrome for this center
            return left + 1, right - 1

        start, end = 0, 0
        for i in range(len(s)):
            l1, r1 = expand(i, i)       # odd-length palindromes centered at i
            l2, r2 = expand(i, i + 1)   # even-length palindromes centered between i, i+1
            if r1 - l1 > end - start:
                start, end = l1, r1
            if r2 - l2 > end - start:
                start, end = l2, r2
        return s[start:end + 1]


if __name__ == "__main__":
    sol = Solution()
    print("expected len 3 palindrome, got", sol.longestPalindrome("babad"))
    print("expected bb, got", sol.longestPalindrome("cbbd"))
    print("expected a, got", sol.longestPalindrome("a"))
