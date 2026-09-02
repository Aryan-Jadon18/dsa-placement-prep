# Suffix max of future prices — Time: O(n), Space: O(n)
from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        if n < 2:
            return 0
        suffix_max = [0] * n
        suffix_max[-1] = prices[-1]
        for i in range(n - 2, -1, -1):
            suffix_max[i] = max(prices[i], suffix_max[i + 1])
        best = 0
        for i in range(n - 1):
            best = max(best, suffix_max[i + 1] - prices[i])
        return best


if __name__ == "__main__":
    sol = Solution()
    print("expected 5, got", sol.maxProfit([7, 1, 5, 3, 6, 4]))
    print("expected 0, got", sol.maxProfit([7, 6, 4, 3, 1]))
    print("expected 2, got", sol.maxProfit([2, 4, 1]))
