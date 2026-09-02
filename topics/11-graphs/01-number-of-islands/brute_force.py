# Recursive DFS with separate visited matrix — Time: O(rows*cols), Space: O(rows*cols)
from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid or not grid[0]:
            return 0
        rows, cols = len(grid), len(grid[0])
        visited = [[False] * cols for _ in range(rows)]

        def dfs(r: int, c: int) -> None:
            if r < 0 or r >= rows or c < 0 or c >= cols:
                return
            if visited[r][c] or grid[r][c] != "1":
                return
            visited[r][c] = True
            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)

        count = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1" and not visited[r][c]:
                    count += 1
                    dfs(r, c)
        return count


if __name__ == "__main__":
    sol = Solution()
    g1 = [list("11000"), list("11000"), list("00100"), list("00011")]
    print("expected 3, got", sol.numIslands(g1))
    print("expected 0, got", sol.numIslands([["0"]]))
    print("expected 1, got", sol.numIslands([["1", "1", "1"]]))
