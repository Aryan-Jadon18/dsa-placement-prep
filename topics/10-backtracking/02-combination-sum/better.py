# Backtracking with non-decreasing start index (no sort) — Time: O(2^target), Space: O(target/min)+output
from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        path = []

        def backtrack(start, remaining):
            if remaining == 0:
                result.append(path[:])
                return
            if remaining < 0:
                return
            for i in range(start, len(candidates)):
                path.append(candidates[i])
                backtrack(i, remaining - candidates[i])  # reuse allowed: stay at i
                path.pop()

        backtrack(0, target)
        return result


if __name__ == "__main__":
    sol = Solution()
    r1 = sorted(sorted(c) for c in sol.combinationSum([2, 3, 6, 7], 7))
    print("expected [[2, 2, 3], [7]], got", r1)

    r2 = sorted(sorted(c) for c in sol.combinationSum([2, 3, 5], 8))
    print("expected [[2, 2, 2, 2], [2, 3, 3], [3, 5]], got", r2)

    r3 = sol.combinationSum([2], 1)
    print("expected [], got", r3)
