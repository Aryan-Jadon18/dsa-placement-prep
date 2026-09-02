# All index-subsets summing to target, dedup via sorted tuples — Time: O(2^n)+dedup, Space: O(2^n*n)
from typing import List


class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        n = len(candidates)
        found = []
        path = []

        def dfs(start, remaining):
            if remaining == 0:
                found.append(path[:])
                return
            if remaining < 0 or start == n:
                return
            for i in range(start, n):
                path.append(candidates[i])
                dfs(i + 1, remaining - candidates[i])
                path.pop()

        dfs(0, target)

        seen = set()
        result = []
        for combo in found:
            key = tuple(sorted(combo))
            if key not in seen:
                seen.add(key)
                result.append(list(key))
        return result


if __name__ == "__main__":
    sol = Solution()
    r1 = sorted(sol.combinationSum2([10, 1, 2, 7, 6, 1, 5], 8))
    print("expected [[1, 1, 6], [1, 2, 5], [1, 7], [2, 6]], got", r1)

    r2 = sorted(sol.combinationSum2([2, 5, 2, 1, 2], 5))
    print("expected [[1, 2, 2], [5]], got", r2)

    r3 = sol.combinationSum2([2], 1)
    print("expected [], got", r3)
