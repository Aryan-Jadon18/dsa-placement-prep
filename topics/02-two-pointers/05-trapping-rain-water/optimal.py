# Two pointers with running left_max/right_max — Time: O(n), Space: O(1)
from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0

        left, right = 0, len(height) - 1
        left_max, right_max = height[left], height[right]
        total = 0

        while left < right:
            if left_max < right_max:
                left += 1
                left_max = max(left_max, height[left])
                total += left_max - height[left]
            else:
                right -= 1
                right_max = max(right_max, height[right])
                total += right_max - height[right]

        return total


if __name__ == "__main__":
    sol = Solution()
    print("expected 6, got", sol.trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]))
    print("expected 9, got", sol.trap([4, 2, 0, 3, 2, 5]))
    print("expected 0, got", sol.trap([1, 2, 3]))
