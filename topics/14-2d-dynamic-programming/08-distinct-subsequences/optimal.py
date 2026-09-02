# Bottom-up tabulation, rolling 1D array (right-to-left update) — Time: O(len(s)*len(t)), Space: O(len(t))
class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        m, n = len(s), len(t)
        dp = [0] * (n + 1)
        dp[0] = 1  # empty target: exactly one way (delete everything)

        for i in range(1, m + 1):
            for j in range(n, 0, -1):  # right-to-left so dp[j-1] is still "row i-1"
                if s[i - 1] == t[j - 1]:
                    dp[j] += dp[j - 1]
        return dp[n]


if __name__ == "__main__":
    sol = Solution()
    print("expected 3, got", sol.numDistinct("rabbbit", "rabbit"))
    print("expected 5, got", sol.numDistinct("babgbag", "bag"))
    print("expected 0, got", sol.numDistinct("abc", "abcd"))
