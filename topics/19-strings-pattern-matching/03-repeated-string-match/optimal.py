# Minimal repeat count + explicit KMP substring search — Time: O(len(a)+len(b)), Space: O(len(a)+len(b))
import math


class Solution:
    def repeatedStringMatch(self, a: str, b: str) -> int:
        min_count = math.ceil(len(b) / len(a))

        if self._contains(a * min_count, b):
            return min_count
        if self._contains(a * (min_count + 1), b):
            return min_count + 1
        return -1

    def _contains(self, haystack: str, needle: str) -> bool:
        n, m = len(haystack), len(needle)
        if m == 0:
            return True
        if m > n:
            return False

        lps = self._build_lps(needle)
        i = j = 0
        while i < n:
            if haystack[i] == needle[j]:
                i += 1
                j += 1
                if j == m:
                    return True
            elif j > 0:
                j = lps[j - 1]
            else:
                i += 1
        return False

    @staticmethod
    def _build_lps(needle: str) -> list:
        m = len(needle)
        lps = [0] * m
        length = 0
        i = 1
        while i < m:
            if needle[i] == needle[length]:
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
    print("Expected: 3, Got:", sol.repeatedStringMatch("abcd", "cdabcdab"))
    print("Expected: 2, Got:", sol.repeatedStringMatch("a", "aa"))
    print("Expected: -1, Got:", sol.repeatedStringMatch("abc", "wxyz"))
