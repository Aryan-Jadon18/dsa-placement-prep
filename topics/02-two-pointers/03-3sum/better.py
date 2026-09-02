# Fix one element, hash-set two-sum on the rest — Time: O(n^2), Space: O(n)
from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        triplets = set()
        for i in range(n):
            target = -nums[i]
            seen = set()
            for j in range(i + 1, n):
                complement = target - nums[j]
                if complement in seen:
                    triplets.add(tuple(sorted((nums[i], nums[j], complement))))
                seen.add(nums[j])
        return [list(t) for t in triplets]


if __name__ == "__main__":
    sol = Solution()
    print(sorted(sol.threeSum([-1, 0, 1, 2, -1, -4])))
    print("expected [], got", sol.threeSum([0, 1, 1]))
    print("expected [[0, 0, 0]], got", sol.threeSum([0, 0, 0]))
