# Union-Find with path compression + union by rank — Time: O(rows*cols*a(rows*cols)), Space: O(rows*cols)
from typing import List


class DSU:
    def __init__(self, n: int) -> None:
        self.parent = list(range(n))
        self.rank = [0] * n
        self.count = 0  # number of distinct components among "activated" land cells

    def add(self, x: int) -> None:
        self.count += 1

    def find(self, x: int) -> int:
        while self.parent[x] != x:
            self.parent[x] = self.parent[self.parent[x]]  # path compression
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
        self.count -= 1


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid or not grid[0]:
            return 0
        rows, cols = len(grid), len(grid[0])
        dsu = DSU(rows * cols)

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] != "1":
                    continue
                dsu.add(r * cols + c)
                # only look right/down since we sweep top-left to bottom-right
                if c + 1 < cols and grid[r][c + 1] == "1":
                    dsu.union(r * cols + c, r * cols + c + 1)
                if r + 1 < rows and grid[r + 1][c] == "1":
                    dsu.union(r * cols + c, (r + 1) * cols + c)
        return dsu.count


if __name__ == "__main__":
    sol = Solution()
    g1 = [list("11000"), list("11000"), list("00100"), list("00011")]
    print("expected 3, got", sol.numIslands(g1))
    print("expected 0, got", sol.numIslands([["0"]]))
    print("expected 1, got", sol.numIslands([["1", "1", "1"]]))
