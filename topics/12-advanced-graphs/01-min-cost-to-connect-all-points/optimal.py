# Prim's algorithm with a min-heap — Time: O(n^2 log n), Space: O(n^2)
import heapq
from typing import List


class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        if n <= 1:
            return 0

        def dist(i: int, j: int) -> int:
            return abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1])

        visited = [False] * n
        heap = [(0, 0)]  # (cost, point index)
        total = 0
        count = 0

        while heap and count < n:
            cost, u = heapq.heappop(heap)
            if visited[u]:
                continue  # lazy deletion of stale entries
            visited[u] = True
            total += cost
            count += 1
            for v in range(n):
                if not visited[v]:
                    heapq.heappush(heap, (dist(u, v), v))
        return total


if __name__ == "__main__":
    sol = Solution()
    print("expected 20, got", sol.minCostConnectPoints([[0, 0], [2, 2], [3, 10], [5, 2], [7, 0]]))
    print("expected 18, got", sol.minCostConnectPoints([[3, 12], [-2, 5], [-4, 1]]))
    print("expected 0, got", sol.minCostConnectPoints([[0, 0]]))
