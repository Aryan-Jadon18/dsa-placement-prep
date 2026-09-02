# Generate all ordered sequences, dedup via sorted tuples — Time: exponential + dedup, Space: exponential
from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        seen = set()
        path = []

        def dfs(remaining):
            if remaining == 0:
                seen.add(tuple(sorted(path)))
                return
            if remaining < 0:
                return
            for c in candidates:
                path.append(c)
                dfs(remaining - c)
                path.pop()

        dfs(target)
        return [list(t) for t in seen]


if __name__ == "__main__":
    sol = Solution()
    r1 = sorted(sorted(c) for c in sol.combinationSum([2, 3, 6, 7], 7))
    print("expected [[2, 2, 3], [7]], got", r1)

    r2 = sorted(sorted(c) for c in sol.combinationSum([2, 3, 5], 8))
    print("expected [[2, 2, 2, 2], [2, 3, 3], [3, 5]], got", r2)

    r3 = sol.combinationSum([2], 1)
    print("expected [], got", r3)
