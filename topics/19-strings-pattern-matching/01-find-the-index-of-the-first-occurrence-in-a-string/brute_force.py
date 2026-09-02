# Try every alignment, compare char by char — Time: O(n*m), Space: O(1)
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        n, m = len(haystack), len(needle)
        if m == 0:
            return 0
        for i in range(n - m + 1):
            match = True
            for j in range(m):
                if haystack[i + j] != needle[j]:
                    match = False
                    break
            if match:
                return i
        return -1


if __name__ == "__main__":
    sol = Solution()
    print("Expected: 0, Got:", sol.strStr("sadbutsad", "sad"))
    print("Expected: -1, Got:", sol.strStr("leetcode", "leeto"))
    print("Expected: 0, Got:", sol.strStr("hello", ""))
