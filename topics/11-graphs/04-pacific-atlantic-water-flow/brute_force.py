# Per-cell forward DFS to each ocean — Time: O((rows*cols)^2), Space: O(rows*cols)
from typing import List


class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        if not heights or not heights[0]:
            return []
        rows, cols = len(heights), len(heights[0])

        def reaches(start_r: int, start_c: int, target) -> bool:
            # target(r, c) -> True if (r, c) is a border cell of the ocean we're checking
            visited = set()
            stack = [(start_r, start_c)]
            while stack:
                r, c = stack.pop()
                if (r, c) in visited:
                    continue
                visited.add((r, c))
                if target(r, c):
                    return True
                for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                    nr, nc = r + dr, c + dc
                    if (
                        0 <= nr < rows
                        and 0 <= nc < cols
                        and (nr, nc) not in visited
                        and heights[nr][nc] <= heights[r][c]
                    ):
                        stack.append((nr, nc))
            return False

        pacific = lambda r, c: r == 0 or c == 0
        atlantic = lambda r, c: r == rows - 1 or c == cols - 1

        result = []
        for r in range(rows):
            for c in range(cols):
                if reaches(r, c, pacific) and reaches(r, c, atlantic):
                    result.append([r, c])
        return result


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
