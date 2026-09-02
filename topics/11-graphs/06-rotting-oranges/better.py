# Multi-source BFS, then rescan for leftover fresh oranges — Time: O(rows*cols), Space: O(rows*cols)
from collections import deque
from typing import List


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        if not grid or not grid[0]:
            return 0
        rows, cols = len(grid), len(grid[0])
        q = deque()
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    q.append((r, c))

        minutes = 0
        while q:
            size = len(q)
            rotted_this_round = False
            for _ in range(size):
                r, c = q.popleft()
                for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1:
                        grid[nr][nc] = 2
                        q.append((nr, nc))
                        rotted_this_round = True
            if rotted_this_round:
                minutes += 1

        if any(grid[r][c] == 1 for r in range(rows) for c in range(cols)):
            return -1
        return minutes


if __name__ == "__main__":
    sol = Solution()
    print("expected 4, got", sol.orangesRotting([[2, 1, 1], [1, 1, 0], [0, 1, 1]]))
    print("expected 0, got", sol.orangesRotting([[0, 2]]))
    print("expected -1, got", sol.orangesRotting([[2, 1, 1], [0, 1, 1], [1, 0, 1]]))
