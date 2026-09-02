# Union-Find with a virtual border node — Time: O(rows*cols*a), Space: O(rows*cols)
from typing import List


class DSU:
    def __init__(self, n: int) -> None:
        self.parent = list(range(n))
        self.rank = [0] * n

    def find(self, x: int) -> int:
        while self.parent[x] != x:
            self.parent[x] = self.parent[self.parent[x]]
            x = self.parent[x]
        return x

    def union(self, a: int, b: int) -> None:
        ra, rb = self.find(a), self.find(b)
        if ra == rb:
            return
        if self.rank[ra] < self.rank[rb]:
            ra, rb = rb, ra
        self.parent[rb] = ra
        if self.rank[ra] == self.rank[rb]:
            self.rank[ra] += 1


class Solution:
    def solve(self, board: List[List[str]]) -> None:
        if not board or not board[0]:
            return
        rows, cols = len(board), len(board[0])
        border_node = rows * cols  # virtual node representing "connected to border"
        dsu = DSU(rows * cols + 1)

        def idx(r: int, c: int) -> int:
            return r * cols + c

        for r in range(rows):
            for c in range(cols):
                if board[r][c] != "O":
                    continue
                if r == 0 or r == rows - 1 or c == 0 or c == cols - 1:
                    dsu.union(idx(r, c), border_node)
                for dr, dc in ((1, 0), (0, 1)):  # only right/down to avoid dup work
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < rows and 0 <= nc < cols and board[nr][nc] == "O":
                        dsu.union(idx(r, c), idx(nr, nc))

        border_root = dsu.find(border_node)
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == "O" and dsu.find(idx(r, c)) != border_root:
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
