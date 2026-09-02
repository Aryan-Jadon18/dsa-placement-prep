# Bottom-up state machine, three rolling scalars — Time: O(n), Space: O(1)
class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        hold, sold, rest = float("-inf"), 0, 0
        for price in prices:
            prev_hold, prev_sold, prev_rest = hold, sold, rest
            hold = max(prev_hold, prev_rest - price)
            sold = prev_hold + price
            rest = max(prev_rest, prev_sold)
        return max(sold, rest)


if __name__ == "__main__":
    sol = Solution()
    print("expected 3, got", sol.maxProfit([1, 2, 3, 0, 2]))
    print("expected 0, got", sol.maxProfit([1]))
    print("expected 3, got", sol.maxProfit([1, 4, 2]))
