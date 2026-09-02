# Nested loops — Time: O(n^2), Space: O(1)
from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        for i in range(n):
            for j in range(i + 1, n):
                if nums[i] + nums[j] == target:
                    return [i, j]
        return []


if __name__ == "__main__":
    sol = Solution()
    print("expected [0, 1], got", sol.twoSum([2, 7, 11, 15], 9))
    print("expected [1, 2], got", sol.twoSum([3, 2, 4], 6))
    print("expected [0, 1], got", sol.twoSum([3, 3], 6))
