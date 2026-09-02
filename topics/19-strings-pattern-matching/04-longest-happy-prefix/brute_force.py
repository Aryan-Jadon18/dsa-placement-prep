# Compare every prefix/suffix pair from longest to shortest — Time: O(n^2), Space: O(n)
class Solution:
    def longestPrefix(self, s: str) -> str:
        n = len(s)
        for length in range(n - 1, 0, -1):
            if s[:length] == s[n - length:]:
                return s[:length]
        return ""


if __name__ == "__main__":
    sol = Solution()
    print("Expected: l, Got:", sol.longestPrefix("level"))
    print("Expected: abab, Got:", sol.longestPrefix("ababab"))
    print("Expected: leet, Got:", sol.longestPrefix("leetcodeleet"))
