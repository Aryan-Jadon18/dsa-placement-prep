# Multi-source DFS from border O's, relabel safe cells — Time: O(rows*cols), Space: O(rows*cols)
from typing import List


class Solution:
    def solve(self, board: List[List[str]]) -> None:
        if not board or not board[0]:
            return
        rows, cols = len(board), len(board[0])

        def dfs(r: int, c: int) -> None:
            if r < 0 or r >= rows or c < 0 or c >= cols or board[r][c] != "O":
                return
            board[r][c] = "S"  # mark safe
            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)

        for r in range(rows):
            dfs(r, 0)
            dfs(r, cols - 1)
        for c in range(cols):
            dfs(0, c)
            dfs(rows - 1, c)

        for r in range(rows):
            for c in range(cols):
                if board[r][c] == "O":
                    board[r][c] = "X"
                elif board[r][c] == "S":
                    board[r][c] = "O"


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
