# Union-Find with size tracking, path compression + union by rank — Time: O(rows*cols*a), Space: O(rows*cols)
from typing import List


class DSU:
    def __init__(self, n: int) -> None:
        self.parent = list(range(n))
        self.rank = [0] * n
        self.size = [0] * n  # 0 until a cell is activated as land

    def activate(self, x: int) -> None:
        self.size[x] = 1

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
        self.size[ra] += self.size[rb]
        if self.rank[ra] == self.rank[rb]:
            self.rank[ra] += 1


class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid or not grid[0]:
            return 0
        rows, cols = len(grid), len(grid[0])
        dsu = DSU(rows * cols)

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] != 1:
                    continue
                dsu.activate(r * cols + c)
                # only union with already-activated neighbors (left/up), since we
                # sweep top-left to bottom-right and size must be set before merging
                if c - 1 >= 0 and grid[r][c - 1] == 1:
                    dsu.union(r * cols + c, r * cols + c - 1)
                if r - 1 >= 0 and grid[r - 1][c] == 1:
                    dsu.union(r * cols + c, (r - 1) * cols + c)

        best = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    root = dsu.find(r * cols + c)
                    best = max(best, dsu.size[root])
        return best


if __name__ == "__main__":
    sol = Solution()
    g1 = [[0, 0, 1, 0], [0, 1, 1, 0], [0, 0, 0, 1]]
    print("expected 3, got", sol.maxAreaOfIsland(g1))
    print("expected 0, got", sol.maxAreaOfIsland([[0, 0], [0, 0]]))
    print("expected 4, got", sol.maxAreaOfIsland([[1, 1], [1, 1]]))
