# Array-based Prim's (no heap) — Time: O(n^2), Space: O(n)
from typing import List


class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        if n <= 1:
            return 0

        def dist(i: int, j: int) -> int:
            return abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1])

        in_mst = [False] * n
        min_dist = [float("inf")] * n
        min_dist[0] = 0
        total = 0

        for _ in range(n):
            u = -1
            for v in range(n):
                if not in_mst[v] and (u == -1 or min_dist[v] < min_dist[u]):
                    u = v
            in_mst[u] = True
            total += min_dist[u]
            for v in range(n):
                if not in_mst[v]:
                    d = dist(u, v)
                    if d < min_dist[v]:
                        min_dist[v] = d
        return total


if __name__ == "__main__":
    sol = Solution()
    print("expected 20, got", sol.minCostConnectPoints([[0, 0], [2, 2], [3, 10], [5, 2], [7, 0]]))
    print("expected 18, got", sol.minCostConnectPoints([[3, 12], [-2, 5], [-4, 1]]))
    print("expected 0, got", sol.minCostConnectPoints([[0, 0]]))
