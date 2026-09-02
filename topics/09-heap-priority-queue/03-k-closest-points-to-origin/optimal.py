# Quickselect on squared distance — Time: O(n) average, O(n^2) worst, Space: O(1) extra
import random
from typing import List


class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        points = list(points)

        def dist(p):
            return p[0] ** 2 + p[1] ** 2

        def partition(lo, hi, pivot_idx):
            pivot_dist = dist(points[pivot_idx])
            points[pivot_idx], points[hi] = points[hi], points[pivot_idx]
            store = lo
            for i in range(lo, hi):
                if dist(points[i]) < pivot_dist:
                    points[i], points[store] = points[store], points[i]
                    store += 1
            points[store], points[hi] = points[hi], points[store]
            return store

        def quickselect(lo, hi, k):
            while lo < hi:
                pivot_idx = random.randint(lo, hi)
                pos = partition(lo, hi, pivot_idx)
                if pos == k:
                    return
                elif pos < k:
                    lo = pos + 1
                else:
                    hi = pos - 1

        quickselect(0, len(points) - 1, k)
        return points[:k]


if __name__ == "__main__":
    sol = Solution()
    print("Expected: [[-2, 2]]  Actual:", sol.kClosest([[1, 3], [-2, 2]], 1))
    print("Expected: {(3, 3), (-2, 4)}  Actual:",
          set(map(tuple, sol.kClosest([[3, 3], [5, -1], [-2, 4]], 2))))
    print("Expected: [[0, 0]]  Actual:", sol.kClosest([[0, 0]], 1))
