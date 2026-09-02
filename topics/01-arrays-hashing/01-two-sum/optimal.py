# One-pass hash map — Time: O(n), Space: O(n)
from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}  # value -> index
        for i, num in enumerate(nums):
            complement = target - num
            if complement in seen:
                return [seen[complement], i]
            seen[num] = i
        return []


if __name__ == "__main__":
    sol = Solution()
    print("expected [0, 1], got", sol.twoSum([2, 7, 11, 15], 9))
    print("expected [1, 2], got", sol.twoSum([3, 2, 4], 6))
    print("expected [0, 1], got", sol.twoSum([3, 3], 6))
