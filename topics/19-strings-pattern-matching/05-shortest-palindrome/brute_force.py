# Check every prefix length for the palindrome property, longest first — Time: O(n^2), Space: O(n)
class Solution:
    def shortestPalindrome(self, s: str) -> str:
        n = len(s)
        if n == 0:
            return s

        for length in range(n, 0, -1):
            prefix = s[:length]
            if prefix == prefix[::-1]:
                remainder = s[length:]
                return remainder[::-1] + s
        return s


if __name__ == "__main__":
    sol = Solution()
    print("Expected: aaacecaaa, Got:", sol.shortestPalindrome("aacecaaa"))
    print("Expected: dcbabcd, Got:", sol.shortestPalindrome("abcd"))
    print("Expected: aba, Got:", sol.shortestPalindrome("aba"))
