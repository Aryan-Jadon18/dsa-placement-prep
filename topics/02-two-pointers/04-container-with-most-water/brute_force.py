# All pairs — Time: O(n^2), Space: O(1)
from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        n = len(height)
        best = 0
        for i in range(n):
            for j in range(i + 1, n):
                area = min(height[i], height[j]) * (j - i)
                best = max(best, area)
        return best


if __name__ == "__main__":
    sol = Solution()
    print("expected 49, got", sol.maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7]))
    print("expected 1, got", sol.maxArea([1, 1]))
    print("expected 16, got", sol.maxArea([4, 3, 2, 1, 4]))
