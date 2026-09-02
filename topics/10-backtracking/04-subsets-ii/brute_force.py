# Generate all subsets ignoring duplicates, dedup via set — Time: O(n*2^n + 2^n*n log n), Space: O(n*2^n)
from typing import List


class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        all_subsets = []
        path = []

        def backtrack(start):
            all_subsets.append(path[:])
            for i in range(start, n):
                path.append(nums[i])
                backtrack(i + 1)
                path.pop()

        backtrack(0)

        seen = set()
        result = []
        for subset in all_subsets:
            key = tuple(sorted(subset))
            if key not in seen:
                seen.add(key)
                result.append(list(key))
        return result


if __name__ == "__main__":
    sol = Solution()
    r1 = sorted(sol.subsetsWithDup([1, 2, 2]))
    print("expected [[], [1], [1, 2], [1, 2, 2], [2], [2, 2]], got", r1)

    r2 = sorted(sol.subsetsWithDup([0]))
    print("expected [[], [0]], got", r2)

    r3 = sorted(sol.subsetsWithDup([4, 4, 4]))
    print("expected [[], [4], [4, 4], [4, 4, 4]], got", r3)
