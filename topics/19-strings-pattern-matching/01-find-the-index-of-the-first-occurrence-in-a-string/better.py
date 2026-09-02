# Rabin-Karp rolling hash — Time: O(n+m) average, O(n*m) worst case, Space: O(1)
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        n, m = len(haystack), len(needle)
        if m == 0:
            return 0
        if m > n:
            return -1

        BASE = 26
        MOD = 2_147_483_647  # large prime-ish modulus to reduce collisions

        needle_hash = 0
        window_hash = 0
        high_order = pow(BASE, m - 1, MOD)

        for i in range(m):
            needle_hash = (needle_hash * BASE + ord(needle[i])) % MOD
            window_hash = (window_hash * BASE + ord(haystack[i])) % MOD

        for i in range(n - m + 1):
            if window_hash == needle_hash and haystack[i:i + m] == needle:
                return i
            if i + m < n:
                window_hash = (window_hash - ord(haystack[i]) * high_order) % MOD
                window_hash = (window_hash * BASE + ord(haystack[i + m])) % MOD
                window_hash %= MOD

        return -1


if __name__ == "__main__":
    sol = Solution()
    print("Expected: 0, Got:", sol.strStr("sadbutsad", "sad"))
    print("Expected: -1, Got:", sol.strStr("leetcode", "leeto"))
    print("Expected: 0, Got:", sol.strStr("hello", ""))
