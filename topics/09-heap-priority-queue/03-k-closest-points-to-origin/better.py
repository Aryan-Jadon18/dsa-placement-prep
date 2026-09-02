# Max-heap capped at size k (negated distances) — Time: O(n log k), Space: O(k)
import heapq
from typing import List


class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        for x, y in points:
            dist = x * x + y * y
            heapq.heappush(heap, (-dist, x, y))
            if len(heap) > k:
                heapq.heappop(heap)
        return [[x, y] for _, x, y in heap]


if __name__ == "__main__":
    sol = Solution()
    print("Expected: [[-2, 2]]  Actual:", sol.kClosest([[1, 3], [-2, 2]], 1))
    print("Expected: {(3, 3), (-2, 4)}  Actual:",
          set(map(tuple, sol.kClosest([[3, 3], [5, -1], [-2, 4]], 2))))
    print("Expected: [[0, 0]]  Actual:", sol.kClosest([[0, 0]], 1))
