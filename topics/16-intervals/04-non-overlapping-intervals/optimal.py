# Greedy: sort by end time, keep earliest-ending compatible interval — Time: O(n log n), Space: O(1)
from typing import List


class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        if not intervals:
            return 0
        intervals.sort(key=lambda iv: iv[1])

        removals = 0
        last_end = float("-inf")
        for start, end in intervals:
            if start >= last_end:
                last_end = end  # compatible, keep it
            else:
                removals += 1  # overlaps the kept interval, must remove

        return removals


if __name__ == "__main__":
    sol = Solution()
    print("Expected: 1, Got:", sol.eraseOverlapIntervals([[1, 2], [2, 3], [3, 4], [1, 3]]))
    print("Expected: 2, Got:", sol.eraseOverlapIntervals([[1, 2], [1, 2], [1, 2]]))
    print("Expected: 0, Got:", sol.eraseOverlapIntervals([[1, 2], [2, 3]]))
