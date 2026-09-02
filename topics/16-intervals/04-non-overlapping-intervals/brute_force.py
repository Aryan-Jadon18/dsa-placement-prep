# Recursive keep/remove over all subsets — Time: O(2^n), Space: O(n)
from typing import List


class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        ordered = sorted(intervals, key=lambda iv: iv[0])
        n = len(ordered)

        def best_kept(i: int, last_end: float) -> int:
            if i == n:
                return 0
            skip = best_kept(i + 1, last_end)
            keep = 0
            if ordered[i][0] >= last_end:
                keep = 1 + best_kept(i + 1, ordered[i][1])
            return max(skip, keep)

        return n - best_kept(0, float("-inf"))


if __name__ == "__main__":
    sol = Solution()
    print("Expected: 1, Got:", sol.eraseOverlapIntervals([[1, 2], [2, 3], [3, 4], [1, 3]]))
    print("Expected: 2, Got:", sol.eraseOverlapIntervals([[1, 2], [1, 2], [1, 2]]))
    print("Expected: 0, Got:", sol.eraseOverlapIntervals([[1, 2], [2, 3]]))
