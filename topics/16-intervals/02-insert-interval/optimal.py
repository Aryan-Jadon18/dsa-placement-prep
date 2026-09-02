# Single pass: before / merge / after — Time: O(n), Space: O(n)
from typing import List


class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        result = []
        i, n = 0, len(intervals)
        start, end = newInterval[0], newInterval[1]

        while i < n and intervals[i][1] < start:
            result.append(intervals[i])
            i += 1

        while i < n and intervals[i][0] <= end:
            start = min(start, intervals[i][0])
            end = max(end, intervals[i][1])
            i += 1
        result.append([start, end])

        while i < n:
            result.append(intervals[i])
            i += 1

        return result


if __name__ == "__main__":
    sol = Solution()
    print("Expected: [[1,5],[6,9]], Got:", sol.insert([[1, 3], [6, 9]], [2, 5]))
    print("Expected: [[1,2],[3,10],[12,16]], Got:",
          sol.insert([[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]], [4, 8]))
    print("Expected: [[5,7]], Got:", sol.insert([], [5, 7]))
