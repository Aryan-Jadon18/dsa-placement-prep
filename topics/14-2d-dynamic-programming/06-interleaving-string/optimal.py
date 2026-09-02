# Bottom-up tabulation, rolling 1D boolean array — Time: O(m*n), Space: O(min(m,n))
class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        m, n = len(s1), len(s2)
        if m + n != len(s3):
            return False
        if m < n:
            s1, s2, m, n = s2, s1, n, m  # keep the inner (shorter) row small

        dp = [False] * (n + 1)
        dp[0] = True
        for j in range(1, n + 1):
            dp[j] = dp[j - 1] and s2[j - 1] == s3[j - 1]

        for i in range(1, m + 1):
            dp[0] = dp[0] and s1[i - 1] == s3[i - 1]
            for j in range(1, n + 1):
                k = i + j - 1
                dp[j] = (dp[j] and s1[i - 1] == s3[k]) or (dp[j - 1] and s2[j - 1] == s3[k])
        return dp[n]


if __name__ == "__main__":
    sol = Solution()
    print("expected True, got", sol.isInterleave("aab", "axy", "aaaxby"))
    print("expected False, got", sol.isInterleave("abc", "xyz", "abcxzy"))
    print("expected True, got", sol.isInterleave("", "abc", "abc"))
