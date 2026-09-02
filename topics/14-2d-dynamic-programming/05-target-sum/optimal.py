# Subset-sum reduction, bottom-up 0/1 knapsack (descending inner loop) — Time: O(n*sum), Space: O(sum)
class Solution:
    def findTargetSumWays(self, nums: list[int], target: int) -> int:
        total = sum(nums)
        if target > total or target < -total or (total + target) % 2 != 0:
            return 0

        p = (total + target) // 2  # size of the "positive" subset
        dp = [0] * (p + 1)
        dp[0] = 1
        for num in nums:
            for j in range(p, num - 1, -1):  # descending: use each num at most once
                dp[j] += dp[j - num]
        return dp[p]


if __name__ == "__main__":
    sol = Solution()
    print("expected 5, got", sol.findTargetSumWays([1, 1, 1, 1, 1], 3))
    print("expected 1, got", sol.findTargetSumWays([1], 1))
    print("expected 2, got", sol.findTargetSumWays([1, 0], 1))
