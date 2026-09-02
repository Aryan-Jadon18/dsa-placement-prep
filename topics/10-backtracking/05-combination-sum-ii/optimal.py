# Sorted + skip duplicates + early break pruning — Time: O(2^n) fewer nodes, Space: O(n)+output
from typing import List


class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        n = len(candidates)
        result = []
        path = []

        def backtrack(start, remaining):
            if remaining == 0:
                result.append(path[:])
                return
            for i in range(start, n):
                if candidates[i] > remaining:
                    break  # sorted: nothing after this can fit either
                if i > start and candidates[i] == candidates[i - 1]:
                    continue
                path.append(candidates[i])
                backtrack(i + 1, remaining - candidates[i])
                path.pop()

        backtrack(0, target)
        return result


if __name__ == "__main__":
    sol = Solution()
    r1 = sorted(sol.combinationSum2([10, 1, 2, 7, 6, 1, 5], 8))
    print("expected [[1, 1, 6], [1, 2, 5], [1, 7], [2, 6]], got", r1)

    r2 = sorted(sol.combinationSum2([2, 5, 2, 1, 2], 5))
    print("expected [[1, 2, 2], [5]], got", r2)

    r3 = sol.combinationSum2([2], 1)
    print("expected [], got", r3)
