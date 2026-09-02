# Backtracking with explicit used[] tracker — Time: O(n! * n), Space: O(n)+output
from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        used = [False] * n
        path = []
        result = []

        def backtrack():
            if len(path) == n:
                result.append(path[:])
                return
            for i in range(n):
                if used[i]:
                    continue
                used[i] = True
                path.append(nums[i])
                backtrack()
                path.pop()
                used[i] = False

        backtrack()
        return result


if __name__ == "__main__":
    sol = Solution()
    r1 = sorted(sol.permute([1, 2, 3]))
    print("expected 6 perms, got", len(r1), r1)

    r2 = sorted(sol.permute([0, 1]))
    print("expected [[0, 1], [1, 0]], got", r2)

    r3 = sol.permute([1])
    print("expected [[1]], got", r3)
