# Iterative BFS, mutating grid in place — Time: O(rows*cols), Space: O(min(rows,cols)) avg
from collections import deque
from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid or not grid[0]:
            return 0
        rows, cols = len(grid), len(grid[0])
        count = 0

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] != "1":
                    continue
                count += 1
                grid[r][c] = "0"  # mark visited immediately
                q = deque([(r, c)])
                while q:
                    cr, cc = q.popleft()
                    for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                        nr, nc = cr + dr, cc + dc
                        if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == "1":
                            grid[nr][nc] = "0"
                            q.append((nr, nc))
        return count


if __name__ == "__main__":
    sol = Solution()
    g1 = [list("11000"), list("11000"), list("00100"), list("00011")]
    print("expected 3, got", sol.numIslands(g1))
    print("expected 0, got", sol.numIslands([["0"]]))
    print("expected 1, got", sol.numIslands([["1", "1", "1"]]))
