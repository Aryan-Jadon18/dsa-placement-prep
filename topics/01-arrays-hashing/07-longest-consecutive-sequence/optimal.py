# Hash set, only expand from true sequence starts — Time: O(n), Space: O(n)
from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        best = 0
        for num in num_set:
            if (num - 1) not in num_set:  # only start counting from a run's beginning
                length = 1
                current = num
                while (current + 1) in num_set:
                    current += 1
                    length += 1
                best = max(best, length)
        return best


if __name__ == "__main__":
    sol = Solution()
    print("expected 4, got", sol.longestConsecutive([100, 4, 200, 1, 3, 2]))
    print("expected 9, got", sol.longestConsecutive([0, 3, 7, 2, 5, 8, 4, 6, 0, 1]))
    print("expected 1, got", sol.longestConsecutive([1, 1, 1, 1]))
