# KMP with a precomputed failure function (LPS array) — Time: O(n+m), Space: O(m)
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        n, m = len(haystack), len(needle)
        if m == 0:
            return 0
        if m > n:
            return -1

        lps = self._build_lps(needle)

        i = j = 0
        while i < n:
            if haystack[i] == needle[j]:
                i += 1
                j += 1
                if j == m:
                    return i - j
            elif j > 0:
                j = lps[j - 1]  # reuse the longest prefix-suffix, no restart from 0
            else:
                i += 1

        return -1

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
    print("Expected: 0, Got:", sol.strStr("sadbutsad", "sad"))
    print("Expected: -1, Got:", sol.strStr("leetcode", "leeto"))
    print("Expected: 0, Got:", sol.strStr("hello", ""))
    print("Expected: 2, Got:", sol.strStr("aaaaab", "aaab"))
