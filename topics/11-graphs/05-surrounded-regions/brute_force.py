# Per-region DFS with border check, no global memo — Time: O((rows*cols)^2), Space: O(rows*cols)
from typing import List


class Solution:
    def solve(self, board: List[List[str]]) -> None:
        if not board or not board[0]:
            return
        rows, cols = len(board), len(board[0])
        safe = set()  # cells confirmed to belong to a border-touching region

        def component_touches_border(r: int, c: int) -> bool:
            # explore the whole component from scratch, ignoring `safe` cache on purpose
            visited = set()
            stack = [(r, c)]
            touches = False
            while stack:
                cr, cc = stack.pop()
                if (cr, cc) in visited:
                    continue
                visited.add((cr, cc))
                if cr == 0 or cr == rows - 1 or cc == 0 or cc == cols - 1:
                    touches = True
                for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                    nr, nc = cr + dr, cc + dc
                    if (
                        0 <= nr < rows
                        and 0 <= nc < cols
                        and (nr, nc) not in visited
                        and board[nr][nc] == "O"
                    ):
                        stack.append((nr, nc))
            if touches:
                safe.update(visited)
            return touches

        for r in range(rows):
            for c in range(cols):
                if board[r][c] == "O" and (r, c) not in safe:
                    component_touches_border(r, c)

        for r in range(rows):
            for c in range(cols):
                if board[r][c] == "O" and (r, c) not in safe:
                    board[r][c] = "X"


if __name__ == "__main__":
    sol = Solution()
    b1 = [
        list("XXXX"),
        list("XOOX"),
        list("XXOX"),
        list("XOXX"),
    ]
    sol.solve(b1)
    expected1 = [list("XXXX"), list("XXXX"), list("XXXX"), list("XOXX")]
    print("expected", expected1)
    print("got     ", b1)

    b2 = [["X"]]
    sol.solve(b2)
    print("expected [['X']], got", b2)

    b3 = [["O", "O"], ["O", "O"]]
    sol.solve(b3)
    print("expected unchanged, got", b3)
