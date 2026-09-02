# XOR of indices and values — Time: O(n), Space: O(1)
from typing import List


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        result = len(nums)  # account for index n (the extra index not paired by enumerate)
        for i, num in enumerate(nums):
            result ^= i ^ num
        return result


if __name__ == "__main__":
    sol = Solution()
    print("expected 2, got", sol.missingNumber([3, 0, 1]))
    print("expected 2, got", sol.missingNumber([0, 1]))
    print("expected 8, got", sol.missingNumber([9, 6, 4, 2, 3, 5, 7, 0, 1]))
