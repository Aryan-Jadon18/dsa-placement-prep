# Bottom-up tabulation, rolling 1D array — Time: O(m*n), Space: O(n)
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [1] * n
        for _ in range(1, m):
            for col in range(1, n):
                dp[col] += dp[col - 1]
        return dp[-1]


if __name__ == "__main__":
    sol = Solution()
    print("expected 28, got", sol.uniquePaths(3, 7))
    print("expected 3, got", sol.uniquePaths(3, 2))
    print("expected 1, got", sol.uniquePaths(1, 1))
