# Iterative BFS, mutating grid in place — Time: O(rows*cols), Space: O(min(rows,cols)) avg
from collections import deque
from typing import List


class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid or not grid[0]:
            return 0
        rows, cols = len(grid), len(grid[0])
        best = 0

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] != 1:
                    continue
                grid[r][c] = 0
                q = deque([(r, c)])
                area = 0
                while q:
                    cr, cc = q.popleft()
                    area += 1
                    for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                        nr, nc = cr + dr, cc + dc
                        if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1:
                            grid[nr][nc] = 0
                            q.append((nr, nc))
                best = max(best, area)
        return best


if __name__ == "__main__":
    sol = Solution()
    g1 = [[0, 0, 1, 0], [0, 1, 1, 0], [0, 0, 0, 1]]
    print("expected 3, got", sol.maxAreaOfIsland(g1))
    print("expected 0, got", sol.maxAreaOfIsland([[0, 0], [0, 0]]))
    print("expected 4, got", sol.maxAreaOfIsland([[1, 1], [1, 1]]))
