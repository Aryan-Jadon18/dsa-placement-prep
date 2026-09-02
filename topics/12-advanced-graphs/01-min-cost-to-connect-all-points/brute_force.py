# Naive Prim's: rescan all crossing pairs every round — Time: O(n^3), Space: O(n)
from typing import List


class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        if n <= 1:
            return 0

        def dist(i: int, j: int) -> int:
            return abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1])

        in_mst = {0}
        total = 0
        while len(in_mst) < n:
            best_cost = float("inf")
            best_j = -1
            for i in in_mst:
                for j in range(n):
                    if j not in in_mst and dist(i, j) < best_cost:
                        best_cost = dist(i, j)
                        best_j = j
            total += best_cost
            in_mst.add(best_j)
        return total


if __name__ == "__main__":
    sol = Solution()
    print("expected 20, got", sol.minCostConnectPoints([[0, 0], [2, 2], [3, 10], [5, 2], [7, 0]]))
    print("expected 18, got", sol.minCostConnectPoints([[3, 12], [-2, 5], [-4, 1]]))
    print("expected 0, got", sol.minCostConnectPoints([[0, 0]]))
