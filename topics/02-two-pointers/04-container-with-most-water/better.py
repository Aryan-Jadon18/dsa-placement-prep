# All pairs with an early-exit bound per left index — Time: O(n^2) worst case, Space: O(1)
from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        n = len(height)
        best = 0
        for i in range(n):
            # widest possible width from i is (n-1-i); if even that can't beat
            # best using height[i] as the cap, no j can help, so stop early.
            if height[i] * (n - 1 - i) <= best:
                continue
            for j in range(i + 1, n):
                area = min(height[i], height[j]) * (j - i)
                best = max(best, area)
        return best


if __name__ == "__main__":
    sol = Solution()
    print("expected 49, got", sol.maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7]))
    print("expected 1, got", sol.maxArea([1, 1]))
    print("expected 16, got", sol.maxArea([4, 3, 2, 1, 4]))
