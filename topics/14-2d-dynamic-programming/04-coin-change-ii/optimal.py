# Bottom-up unbounded knapsack, coins outer / amount inner — Time: O(len(coins)*amount), Space: O(amount)
class Solution:
    def change(self, amount: int, coins: list[int]) -> int:
        dp = [0] * (amount + 1)
        dp[0] = 1
        for coin in coins:
            for x in range(coin, amount + 1):
                dp[x] += dp[x - coin]
        return dp[amount]


if __name__ == "__main__":
    sol = Solution()
    print("expected 4, got", sol.change(5, [1, 2, 5]))
    print("expected 0, got", sol.change(3, [2]))
    print("expected 1, got", sol.change(0, [1, 2, 3]))
