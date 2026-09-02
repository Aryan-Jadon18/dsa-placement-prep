# Try every buy/sell pair — Time: O(n^2), Space: O(1)
from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        best = 0
        n = len(prices)
        for buy in range(n):
            for sell in range(buy + 1, n):
                best = max(best, prices[sell] - prices[buy])
        return best


if __name__ == "__main__":
    sol = Solution()
    print("expected 5, got", sol.maxProfit([7, 1, 5, 3, 6, 4]))
    print("expected 0, got", sol.maxProfit([7, 6, 4, 3, 1]))
    print("expected 2, got", sol.maxProfit([2, 4, 1]))
