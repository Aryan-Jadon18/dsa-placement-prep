# In-place swapping backtracking, no auxiliary tracker — Time: O(n! * n), Space: O(n)+output
from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        result = []

        def backtrack(start):
            if start == n:
                result.append(nums[:])
                return
            for i in range(start, n):
                nums[start], nums[i] = nums[i], nums[start]
                backtrack(start + 1)
                nums[start], nums[i] = nums[i], nums[start]  # swap back

        backtrack(0)
        return result


if __name__ == "__main__":
    sol = Solution()
    r1 = sorted(sol.permute([1, 2, 3]))
    print("expected 6 perms, got", len(r1), r1)

    r2 = sorted(sol.permute([0, 1]))
    print("expected [[0, 1], [1, 0]], got", r2)

    r3 = sol.permute([1])
    print("expected [[1]], got", r3)
