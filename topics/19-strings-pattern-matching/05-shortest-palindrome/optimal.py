# KMP failure function on s + '#' + reverse(s) — Time: O(n), Space: O(n)
class Solution:
    def shortestPalindrome(self, s: str) -> str:
        n = len(s)
        if n == 0:
            return s

        combined = s + "#" + s[::-1]
        lps = self._build_lps(combined)

        longest_palindromic_prefix_len = lps[-1]
        remainder = s[longest_palindromic_prefix_len:]
        return remainder[::-1] + s

    @staticmethod
    def _build_lps(text: str) -> list:
        m = len(text)
        lps = [0] * m
        length = 0
        i = 1
        while i < m:
            if text[i] == text[length]:
                length += 1
                lps[i] = length
                i += 1
            elif length > 0:
                length = lps[length - 1]
            else:
                lps[i] = 0
                i += 1
        return lps


if __name__ == "__main__":
    sol = Solution()
    print("Expected: aaacecaaa, Got:", sol.shortestPalindrome("aacecaaa"))
    print("Expected: dcbabcd, Got:", sol.shortestPalindrome("abcd"))
    print("Expected: aba, Got:", sol.shortestPalindrome("aba"))
    print("Expected: (empty), Got:", repr(sol.shortestPalindrome("")))
