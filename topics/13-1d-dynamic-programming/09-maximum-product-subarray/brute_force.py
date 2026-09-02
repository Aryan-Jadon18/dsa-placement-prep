# Extend product over every subarray — Time: O(n^2), Space: O(1)
from typing import List


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        n = len(nums)
        best = nums[0]
        for i in range(n):
            product = 1
            for j in range(i, n):
                product *= nums[j]
                best = max(best, product)
        return best


if __name__ == "__main__":
    sol = Solution()
    print("expected 6, got", sol.maxProduct([2, 3, -2, 4]))
    print("expected 0, got", sol.maxProduct([-2, 0, -1]))
    print("expected 24, got", sol.maxProduct([-2, 3, -4]))
