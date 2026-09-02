# Sort, then single pass comparing only to the last merged interval — Time: O(n log n), Space: O(n)
from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        ordered = sorted(intervals, key=lambda iv: iv[0])
        result: List[List[int]] = []

        for start, end in ordered:
            if result and start <= result[-1][1]:
                result[-1][1] = max(result[-1][1], end)
            else:
                result.append([start, end])

        return result


if __name__ == "__main__":
    sol = Solution()
    print("Expected: [[1,6],[8,10],[15,18]], Got:",
          sol.merge([[1, 3], [2, 6], [8, 10], [15, 18]]))
    print("Expected: [[1,5]], Got:", sol.merge([[1, 4], [4, 5]]))
    print("Expected: [[0,4]], Got:", sol.merge([[1, 4], [0, 4]]))
