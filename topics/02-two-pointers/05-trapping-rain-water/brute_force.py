# Recompute left-max/right-max per index by scanning outward — Time: O(n^2), Space: O(1)
from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        total = 0
        for i in range(n):
            left_max = max(height[:i + 1])
            right_max = max(height[i:])
            total += min(left_max, right_max) - height[i]
        return total


if __name__ == "__main__":
    sol = Solution()
    print("expected 6, got", sol.trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]))
    print("expected 9, got", sol.trap([4, 2, 0, 3, 2, 5]))
    print("expected 0, got", sol.trap([1, 2, 3]))
