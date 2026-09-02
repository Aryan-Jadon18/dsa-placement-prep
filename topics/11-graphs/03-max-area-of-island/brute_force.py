# Recursive DFS with separate visited matrix — Time: O(rows*cols), Space: O(rows*cols)
from typing import List


class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid or not grid[0]:
            return 0
        rows, cols = len(grid), len(grid[0])
        visited = [[False] * cols for _ in range(rows)]

        def dfs(r: int, c: int) -> int:
            if r < 0 or r >= rows or c < 0 or c >= cols:
                return 0
            if visited[r][c] or grid[r][c] != 1:
                return 0
            visited[r][c] = True
            return 1 + dfs(r + 1, c) + dfs(r - 1, c) + dfs(r, c + 1) + dfs(r, c - 1)

        best = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1 and not visited[r][c]:
                    best = max(best, dfs(r, c))
        return best


if __name__ == "__main__":
    sol = Solution()
    g1 = [[0, 0, 1, 0], [0, 1, 1, 0], [0, 0, 0, 1]]
    print("expected 3, got", sol.maxAreaOfIsland(g1))
    print("expected 0, got", sol.maxAreaOfIsland([[0, 0], [0, 0]]))
    print("expected 4, got", sol.maxAreaOfIsland([[1, 1], [1, 1]]))
