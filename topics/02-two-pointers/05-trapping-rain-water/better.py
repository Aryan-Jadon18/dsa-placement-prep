# Precomputed left-max and right-max arrays — Time: O(n), Space: O(n)
from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        if n == 0:
            return 0

        left_max = [0] * n
        right_max = [0] * n

        left_max[0] = height[0]
        for i in range(1, n):
            left_max[i] = max(left_max[i - 1], height[i])

        right_max[n - 1] = height[n - 1]
        for i in range(n - 2, -1, -1):
            right_max[i] = max(right_max[i + 1], height[i])

        return sum(min(left_max[i], right_max[i]) - height[i] for i in range(n))


if __name__ == "__main__":
    sol = Solution()
    print("expected 6, got", sol.trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]))
    print("expected 9, got", sol.trap([4, 2, 0, 3, 2, 5]))
    print("expected 0, got", sol.trap([1, 2, 3]))
