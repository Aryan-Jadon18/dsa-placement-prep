# Full sort by squared distance — Time: O(n log n), Space: O(n)
from typing import List


class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        sorted_points = sorted(points, key=lambda p: p[0] ** 2 + p[1] ** 2)
        return sorted_points[:k]


if __name__ == "__main__":
    sol = Solution()
    print("Expected: [[-2, 2]]  Actual:", sol.kClosest([[1, 3], [-2, 2]], 1))
    print("Expected: [[3, 3], [-2, 4]]  Actual:",
          sol.kClosest([[3, 3], [5, -1], [-2, 4]], 2))
    print("Expected: [[0, 0]]  Actual:", sol.kClosest([[0, 0]], 1))
