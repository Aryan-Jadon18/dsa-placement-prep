# Per-bar independent left/right expansion at its own height — Time: O(n^2) worst case, Space: O(1) extra
from typing import List


class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        best = 0
        for i in range(n):
            h = heights[i]
            left = i
            while left - 1 >= 0 and heights[left - 1] >= h:
                left -= 1
            right = i
            while right + 1 < n and heights[right + 1] >= h:
                right += 1
            width = right - left + 1
            best = max(best, h * width)
        return best


if __name__ == "__main__":
    sol = Solution()
    print("expected 10, got", sol.largestRectangleArea([2, 1, 5, 6, 2, 3]))
    print("expected 4, got", sol.largestRectangleArea([2, 4]))
    print("expected 16, got", sol.largestRectangleArea([6, 7, 5, 2, 4, 5, 9, 3]))
