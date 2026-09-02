# Bottom-up interval DP, filled by increasing interval length — Time: O(n^3), Space: O(n^2)
class Solution:
    def maxCoins(self, nums: list[int]) -> int:
        vals = [1] + nums + [1]
        n = len(vals)
        dp = [[0] * n for _ in range(n)]

        for length in range(2, n):  # interval width, right - left
            for left in range(0, n - length):
                right = left + length
                best = 0
                for k in range(left + 1, right):
                    gain = vals[left] * vals[k] * vals[right] + dp[left][k] + dp[k][right]
                    if gain > best:
                        best = gain
                dp[left][right] = best

        return dp[0][n - 1]


if __name__ == "__main__":
    sol = Solution()
    print("expected 167, got", sol.maxCoins([3, 1, 5, 8]))
    print("expected 10, got", sol.maxCoins([1, 5]))
    print("expected 7, got", sol.maxCoins([7]))
