# Check every interval for every query — Time: O(n*q), Space: O(1) extra
from typing import List


class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        answers = []
        for q in queries:
            best = -1
            for left, right in intervals:
                if left <= q <= right:
                    size = right - left + 1
                    if best == -1 or size < best:
                        best = size
            answers.append(best)
        return answers


if __name__ == "__main__":
    sol = Solution()
    print("Expected: [3,3,1,4], Got:",
          sol.minInterval([[1, 4], [2, 4], [3, 6], [4, 4]], [2, 3, 4, 5]))
    print("Expected: [2,-1,4,6], Got:",
          sol.minInterval([[2, 3], [2, 5], [1, 8], [20, 25]], [2, 19, 5, 22]))
    print("Expected: [10], Got:", sol.minInterval([[1, 10]], [5]))
