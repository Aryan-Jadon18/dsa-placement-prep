# Single pass, track min-so-far — Time: O(n), Space: O(1)
from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = float("inf")
        best = 0
        for price in prices:
            if price < min_price:
                min_price = price
            else:
                best = max(best, price - min_price)
        return best


if __name__ == "__main__":
    sol = Solution()
    print("expected 5, got", sol.maxProfit([7, 1, 5, 3, 6, 4]))
    print("expected 0, got", sol.maxProfit([7, 6, 4, 3, 1]))
    print("expected 2, got", sol.maxProfit([2, 4, 1]))
