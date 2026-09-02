# Manacher's algorithm to find the longest palindromic prefix — Time: O(n), Space: O(n)
class Solution:
    def shortestPalindrome(self, s: str) -> str:
        n = len(s)
        if n == 0:
            return s

        # Transform with separators so every palindrome (odd/even) has an odd-length form.
        t = "#" + "#".join(s) + "#"
        m = len(t)
        radius = [0] * m
        center = right = 0

        for i in range(m):
            mirror = 2 * center - i
            if i < right:
                radius[i] = min(right - i, radius[mirror])
            a, b = i + radius[i] + 1, i - radius[i] - 1
            while a < m and b >= 0 and t[a] == t[b]:
                radius[i] += 1
                a += 1
                b -= 1
            if i + radius[i] > right:
                center, right = i, i + radius[i]

        # A palindrome centered at i starts at original index (i - radius[i]) // 2.
        # We want it to start at index 0, i.e. i == radius[i]; take the max such radius.
        best_len = 0
        for i in range(m):
            if i == radius[i]:
                best_len = max(best_len, radius[i])

        remainder = s[best_len:]
        return remainder[::-1] + s


if __name__ == "__main__":
    sol = Solution()
    print("Expected: aaacecaaa, Got:", sol.shortestPalindrome("aacecaaa"))
    print("Expected: dcbabcd, Got:", sol.shortestPalindrome("abcd"))
    print("Expected: aba, Got:", sol.shortestPalindrome("aba"))
