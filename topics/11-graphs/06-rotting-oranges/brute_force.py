# Minute-by-minute full grid simulation — Time: O((rows*cols)^2), Space: O(rows*cols)
import copy
from typing import List


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        if not grid or not grid[0]:
            return 0
        rows, cols = len(grid), len(grid[0])
        minutes = 0

        while True:
            rotten = [(r, c) for r in range(rows) for c in range(cols) if grid[r][c] == 2]
            new_grid = copy.deepcopy(grid)
            changed = False
            for r, c in rotten:
                for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1:
                        new_grid[nr][nc] = 2
                        changed = True
            grid = new_grid
            if not changed:
                break
            minutes += 1

        if any(grid[r][c] == 1 for r in range(rows) for c in range(cols)):
            return -1
        return minutes


if __name__ == "__main__":
    sol = Solution()
    print("expected 4, got", sol.orangesRotting([[2, 1, 1], [1, 1, 0], [0, 1, 1]]))
    print("expected 0, got", sol.orangesRotting([[0, 2]]))
    print("expected -1, got", sol.orangesRotting([[2, 1, 1], [0, 1, 1], [1, 0, 1]]))
