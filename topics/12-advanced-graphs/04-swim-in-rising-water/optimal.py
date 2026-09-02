# Dijkstra-style minimax path with a min-heap — Time: O(n^2 log n), Space: O(n^2)
import heapq
from typing import List


class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        n = len(grid)
        visited = [[False] * n for _ in range(n)]
        heap = [(grid[0][0], 0, 0)]

        while heap:
            cost, r, c = heapq.heappop(heap)
            if visited[r][c]:
                continue
            visited[r][c] = True
            if (r, c) == (n - 1, n - 1):
                return cost
            for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                nr, nc = r + dr, c + dc
                if 0 <= nr < n and 0 <= nc < n and not visited[nr][nc]:
                    heapq.heappush(heap, (max(cost, grid[nr][nc]), nr, nc))

        return -1  # unreachable (won't happen on a full grid)


if __name__ == "__main__":
    sol = Solution()
    print("expected 3, got", sol.swimInWater([[0, 2], [1, 3]]))
    grid2 = [
        [0, 1, 2, 3, 4],
        [24, 23, 22, 21, 5],
        [12, 13, 14, 15, 16],
        [11, 17, 18, 19, 20],
        [10, 9, 8, 7, 6],
    ]
    print("expected 16, got", sol.swimInWater(grid2))
    print("expected 0, got", sol.swimInWater([[0]]))
