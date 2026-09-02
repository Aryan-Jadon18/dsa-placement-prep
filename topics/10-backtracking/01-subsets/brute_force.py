# Bitmasking over all 2^n masks — Time: O(n * 2^n), Space: O(n * 2^n)
from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        result = []
        for mask in range(1 << n):
            subset = [nums[i] for i in range(n) if mask & (1 << i)]
            result.append(subset)
        return result


if __name__ == "__main__":
    sol = Solution()
    print("expected 8 subsets, got", len(sol.subsets([1, 2, 3])), sol.subsets([1, 2, 3]))
    print("expected [[], [0]], got", sol.subsets([0]))
    print("expected 4 subsets, got", len(sol.subsets([1, 2])), sol.subsets([1, 2]))
