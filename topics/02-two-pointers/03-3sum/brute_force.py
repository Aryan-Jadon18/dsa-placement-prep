# Three nested loops + dedupe set — Time: O(n^3), Space: O(n)
from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        triplets = set()
        for i in range(n):
            for j in range(i + 1, n):
                for k in range(j + 1, n):
                    if nums[i] + nums[j] + nums[k] == 0:
                        triplets.add(tuple(sorted((nums[i], nums[j], nums[k]))))
        return [list(t) for t in triplets]


if __name__ == "__main__":
    sol = Solution()
    print(sorted(sol.threeSum([-1, 0, 1, 2, -1, -4])))
    print("expected [], got", sol.threeSum([0, 1, 1]))
    print("expected [[0, 0, 0]], got", sol.threeSum([0, 0, 0]))
