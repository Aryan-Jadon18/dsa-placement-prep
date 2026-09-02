# Plain recursion over (day, holding) — Time: O(2^n), Space: O(n)
class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        n = len(prices)

        def dfs(day: int, holding: bool) -> int:
            if day >= n:
                return 0
            skip = dfs(day + 1, holding)
            if holding:
                act = prices[day] + dfs(day + 2, False)  # sell -> forced 1-day cooldown
            else:
                act = -prices[day] + dfs(day + 1, True)  # buy
            return max(skip, act)

        return dfs(0, False)


if __name__ == "__main__":
    sol = Solution()
    print("expected 3, got", sol.maxProfit([1, 2, 3, 0, 2]))
    print("expected 0, got", sol.maxProfit([1]))
    print("expected 3, got", sol.maxProfit([1, 4, 2]))
