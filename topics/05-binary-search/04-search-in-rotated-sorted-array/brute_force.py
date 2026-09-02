# Linear scan — Time: O(n), Space: O(1)
from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        for i, num in enumerate(nums):
            if num == target:
                return i
        return -1


if __name__ == "__main__":
    sol = Solution()
    print("expected 4, got", sol.search([4, 5, 6, 7, 0, 1, 2], 0))
    print("expected -1, got", sol.search([4, 5, 6, 7, 0, 1, 2], 3))
    print("expected -1, got", sol.search([1], 0))
