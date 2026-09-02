# Multi-source reverse-flow BFS from each ocean's border — Time: O(rows*cols), Space: O(rows*cols)
from collections import deque
from typing import List


class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        if not heights or not heights[0]:
            return []
        rows, cols = len(heights), len(heights[0])

        def bfs(starts):
            visited = set(starts)
            q = deque(starts)
            while q:
                r, c = q.popleft()
                for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                    nr, nc = r + dr, c + dc
                    if (
                        0 <= nr < rows
                        and 0 <= nc < cols
                        and (nr, nc) not in visited
                        and heights[nr][nc] >= heights[r][c]  # reverse flow: uphill
                    ):
                        visited.add((nr, nc))
                        q.append((nr, nc))
            return visited

        pacific_starts = [(0, c) for c in range(cols)] + [(r, 0) for r in range(rows)]
        atlantic_starts = [(rows - 1, c) for c in range(cols)] + [(r, cols - 1) for r in range(rows)]

        pacific = bfs(pacific_starts)
        atlantic = bfs(atlantic_starts)

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
