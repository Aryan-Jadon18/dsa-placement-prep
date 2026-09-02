# Extend each number step by step using linear membership checks — Time: O(n^2)-O(n^3), Space: O(1) extra
from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        best = 0
        for num in nums:
            length = 1
            current = num
            while (current + 1) in nums:  # O(n) linear search each check
                current += 1
                length += 1
            best = max(best, length)
        return best


if __name__ == "__main__":
    sol = Solution()
    print("expected 4, got", sol.longestConsecutive([100, 4, 200, 1, 3, 2]))
    print("expected 9, got", sol.longestConsecutive([0, 3, 7, 2, 5, 8, 4, 6, 0, 1]))
    print("expected 1, got", sol.longestConsecutive([1, 1, 1, 1]))
