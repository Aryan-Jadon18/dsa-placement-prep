# Monotonic increasing stack with a sentinel bar — Time: O(n), Space: O(n)
from typing import List


class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []  # indices, heights strictly increasing
        best = 0
        extended = list(heights) + [0]  # sentinel flushes the stack at the end
        for i, h in enumerate(extended):
            while stack and extended[stack[-1]] > h:
                height = extended[stack.pop()]
                left_bound = stack[-1] if stack else -1
                width = i - left_bound - 1
                best = max(best, height * width)
            stack.append(i)
        return best


if __name__ == "__main__":
    sol = Solution()
    print("expected 10, got", sol.largestRectangleArea([2, 1, 5, 6, 2, 3]))
    print("expected 4, got", sol.largestRectangleArea([2, 4]))
    print("expected 16, got", sol.largestRectangleArea([6, 7, 5, 2, 4, 5, 9, 3]))
