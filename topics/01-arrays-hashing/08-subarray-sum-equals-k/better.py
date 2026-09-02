# Precomputed prefix-sum array, O(1) range sums but still all pairs — Time: O(n^2), Space: O(n)
from typing import List


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        n = len(nums)
        prefix = [0] * (n + 1)
        for i in range(n):
            prefix[i + 1] = prefix[i] + nums[i]

        count = 0
        for i in range(n):
            for j in range(i, n):
                if prefix[j + 1] - prefix[i] == k:
                    count += 1
        return count


if __name__ == "__main__":
    sol = Solution()
    print("expected 2, got", sol.subarraySum([1, 1, 1], 2))
    print("expected 2, got", sol.subarraySum([1, 2, 3], 3))
    print("expected 3, got", sol.subarraySum([1, -1, 0], 0))
