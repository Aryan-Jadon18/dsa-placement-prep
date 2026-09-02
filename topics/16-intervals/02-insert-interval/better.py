# bisect.insort then a single merge sweep — Time: O(n), Space: O(n)
import bisect
from typing import List


class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        starts = [iv[0] for iv in intervals]
        idx = bisect.bisect_left(starts, newInterval[0])
        combined = intervals[:idx] + [newInterval] + intervals[idx:]

        merged = []
        for iv in combined:
            if merged and iv[0] <= merged[-1][1]:
                merged[-1][1] = max(merged[-1][1], iv[1])
            else:
                merged.append(iv[:])
        return merged


if __name__ == "__main__":
    sol = Solution()
    print("Expected: [[1,5],[6,9]], Got:", sol.insert([[1, 3], [6, 9]], [2, 5]))
    print("Expected: [[1,2],[3,10],[12,16]], Got:",
          sol.insert([[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]], [4, 8]))
    print("Expected: [[5,7]], Got:", sol.insert([], [5, 7]))
