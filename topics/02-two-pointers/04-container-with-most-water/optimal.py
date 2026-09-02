# Two pointers, always move the shorter line inward — Time: O(n), Space: O(1)
from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        left, right = 0, len(height) - 1
        best = 0
        while left < right:
            area = min(height[left], height[right]) * (right - left)
            best = max(best, area)
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return best


if __name__ == "__main__":
    sol = Solution()
    print("expected 49, got", sol.maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7]))
    print("expected 1, got", sol.maxArea([1, 1]))
    print("expected 16, got", sol.maxArea([4, 3, 2, 1, 4]))
