# Bottom-up tabulation, O(1) space — Time: O(n), Space: O(1)
class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 1:
            return 1
        # prev2 = dp[i-2], prev1 = dp[i-1]
        prev2, prev1 = 1, 1
        for _ in range(2, n + 1):
            prev2, prev1 = prev1, prev1 + prev2
        return prev1


if __name__ == "__main__":
    sol = Solution()
    print("expected 2, got", sol.climbStairs(2))
    print("expected 3, got", sol.climbStairs(3))
    print("expected 8, got", sol.climbStairs(5))
