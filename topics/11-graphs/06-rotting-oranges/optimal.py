# Multi-source BFS with running fresh-orange counter — Time: O(rows*cols), Space: O(rows*cols)
from collections import deque
from typing import List


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        if not grid or not grid[0]:
            return 0
        rows, cols = len(grid), len(grid[0])
        q = deque()
        fresh = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    q.append((r, c))
                elif grid[r][c] == 1:
                    fresh += 1

        if fresh == 0:
            return 0

        minutes = 0
        while q and fresh > 0:
            size = len(q)
            for _ in range(size):
                r, c = q.popleft()
                for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1:
                        grid[nr][nc] = 2
                        fresh -= 1
                        q.append((nr, nc))
            minutes += 1

        return minutes if fresh == 0 else -1


if __name__ == "__main__":
    sol = Solution()
    print("expected 4, got", sol.orangesRotting([[2, 1, 1], [1, 1, 0], [0, 1, 1]]))
    print("expected 0, got", sol.orangesRotting([[0, 2]]))
    print("expected -1, got", sol.orangesRotting([[2, 1, 1], [0, 1, 1], [1, 0, 1]]))
