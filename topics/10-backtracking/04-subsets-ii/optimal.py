# Group by distinct value, choose a count for each — Time: O(n*2^n), Space: O(n)+output
from collections import Counter
from typing import List


class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        counts = sorted(Counter(nums).items())  # [(value, occurrences), ...]
        result = []
        path = []

        def backtrack(idx):
            if idx == len(counts):
                result.append(path[:])
                return
            value, occurrences = counts[idx]
            for take in range(occurrences + 1):
                path.extend([value] * take)
                backtrack(idx + 1)
                del path[len(path) - take:]

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
