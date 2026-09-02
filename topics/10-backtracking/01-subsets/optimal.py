# Backtracking DFS with shared path (include/exclude) — Time: O(n * 2^n), Space: O(n)+output
from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []
        path = []

        def backtrack(start):
            result.append(path[:])
            for i in range(start, len(nums)):
                path.append(nums[i])
                backtrack(i + 1)
                path.pop()

        backtrack(0)
        return result


if __name__ == "__main__":
    sol = Solution()
    print("expected 8 subsets, got", len(sol.subsets([1, 2, 3])), sol.subsets([1, 2, 3]))
    print("expected [[], [0]], got", sol.subsets([0]))
    print("expected 4 subsets, got", len(sol.subsets([1, 2])), sol.subsets([1, 2]))
