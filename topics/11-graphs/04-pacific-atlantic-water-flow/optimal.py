# Multi-source reverse-flow DFS from each ocean's border — Time: O(rows*cols), Space: O(rows*cols)
from typing import List


class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        if not heights or not heights[0]:
            return []
        rows, cols = len(heights), len(heights[0])

        def dfs(r: int, c: int, visited: set) -> None:
            visited.add((r, c))
            for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                nr, nc = r + dr, c + dc
                if (
                    0 <= nr < rows
                    and 0 <= nc < cols
                    and (nr, nc) not in visited
                    and heights[nr][nc] >= heights[r][c]
                ):
                    dfs(nr, nc, visited)

        pacific, atlantic = set(), set()
        for c in range(cols):
            dfs(0, c, pacific)
            dfs(rows - 1, c, atlantic)
        for r in range(rows):
            dfs(r, 0, pacific)
            dfs(r, cols - 1, atlantic)

        return [[r, c] for r, c in (pacific & atlantic)]


if __name__ == "__main__":
    sol = Solution()
    print("expected [[0, 0]], got", sol.pacificAtlantic([[5]]))

    g2 = [
        [1, 2, 2, 3, 5],
        [3, 2, 3, 4, 4],
        [2, 4, 5, 3, 1],
        [6, 7, 1, 4, 5],
        [5, 1, 1, 2, 4],
    ]
    expected2 = sorted(map(tuple, [[0,4],[1,3],[1,4],[2,2],[3,0],[3,1],[4,0]]))
    got2 = sorted(map(tuple, sol.pacificAtlantic(g2)))
    print("expected", expected2)
    print("got     ", got2)

    g3 = [[1, 1], [1, 1]]
    print("expected all 4 cells, got", sorted(map(tuple, sol.pacificAtlantic(g3))))
