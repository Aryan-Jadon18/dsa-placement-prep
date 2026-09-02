# Every (left, right) pair, min height tracked while expanding right — Time: O(n^2), Space: O(1) extra
from typing import List


class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        best = 0
        for left in range(n):
            min_height = heights[left]
            for right in range(left, n):
                min_height = min(min_height, heights[right])
                width = right - left + 1
                best = max(best, min_height * width)
        return best


if __name__ == "__main__":
    sol = Solution()
    print("expected 10, got", sol.largestRectangleArea([2, 1, 5, 6, 2, 3]))
    print("expected 4, got", sol.largestRectangleArea([2, 4]))
    print("expected 16, got", sol.largestRectangleArea([6, 7, 5, 2, 4, 5, 9, 3]))
