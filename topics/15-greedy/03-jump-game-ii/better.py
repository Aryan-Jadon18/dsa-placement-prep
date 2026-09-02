# DP: relax min jumps to every reachable index — Time: O(n^2), Space: O(n)
class Solution:
    def jump(self, nums: list[int]) -> int:
        n = len(nums)
        dp = [float("inf")] * n
        dp[0] = 0
        for i in range(n):
            if dp[i] == float("inf"):
                continue
            for j in range(i + 1, min(i + nums[i], n - 1) + 1):
                dp[j] = min(dp[j], dp[i] + 1)
        return dp[n - 1]


if __name__ == "__main__":
    sol = Solution()
    print("expected 2, got", sol.jump([2, 3, 1, 1, 4]))
    print("expected 2, got", sol.jump([2, 3, 0, 1, 4]))
    print("expected 0, got", sol.jump([0]))
