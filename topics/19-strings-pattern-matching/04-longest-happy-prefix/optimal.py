# KMP failure function (LPS array), answer is its last entry — Time: O(n), Space: O(n)
class Solution:
    def longestPrefix(self, s: str) -> str:
        n = len(s)
        lps = [0] * n
        length = 0
        i = 1

        while i < n:
            if s[i] == s[length]:
                length += 1
                lps[i] = length
                i += 1
            elif length > 0:
                length = lps[length - 1]
            else:
                lps[i] = 0
                i += 1

        return s[:lps[-1]] if n > 0 else ""


if __name__ == "__main__":
    sol = Solution()
    print("Expected: l, Got:", sol.longestPrefix("level"))
    print("Expected: abab, Got:", sol.longestPrefix("ababab"))
    print("Expected: leet, Got:", sol.longestPrefix("leetcodeleet"))
    print("Expected: (empty), Got:", repr(sol.longestPrefix("abcde")))
