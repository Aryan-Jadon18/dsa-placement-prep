# Sort + skip adjacent duplicates at same recursion level — Time: O(n*2^n), Space: O(n)+output
from typing import List


class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []
        path = []
        n = len(nums)

        def backtrack(start):
            result.append(path[:])
            for i in range(start, n):
                if i > start and nums[i] == nums[i - 1]:
                    continue  # skip duplicate sibling choice at this level
                path.append(nums[i])
                backtrack(i + 1)
                path.pop()

        backtrack(0)
        return result


if __name__ == "__main__":
    sol = Solution()
    r1 = sorted(sol.subsetsWithDup([1, 2, 2]))
    print("expected [[], [1], [1, 2], [1, 2, 2], [2], [2, 2]], got", r1)

    r2 = sorted(sol.subsetsWithDup([0]))
    print("expected [[], [0]], got", r2)

    r3 = sorted(sol.subsetsWithDup([4, 4, 4]))
    print("expected [[], [4], [4, 4], [4, 4, 4]], got", r3)
