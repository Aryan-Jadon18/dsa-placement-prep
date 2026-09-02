# DP: mark every reachable index left to right — Time: O(n^2), Space: O(n)
class Solution:
    def canJump(self, nums: list[int]) -> bool:
        n = len(nums)
        dp = [False] * n
        dp[0] = True
        for i in range(n):
            if not dp[i]:
                continue
            for j in range(i + 1, min(i + nums[i], n - 1) + 1):
                dp[j] = True
        return dp[n - 1]


if __name__ == "__main__":
    sol = Solution()
    print("expected True, got", sol.canJump([2, 3, 1, 1, 4]))
    print("expected False, got", sol.canJump([3, 2, 1, 0, 4]))
    print("expected True, got", sol.canJump([0]))
