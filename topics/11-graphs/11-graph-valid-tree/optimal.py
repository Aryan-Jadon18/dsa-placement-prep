# Union-Find with path compression + union by rank — Time: O(n*a(n)), Space: O(n)
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

    def union(self, a: int, b: int) -> bool:
        ra, rb = self.find(a), self.find(b)
        if ra == rb:
            return False
        if self.rank[ra] < self.rank[rb]:
            ra, rb = rb, ra
        self.parent[rb] = ra
        if self.rank[ra] == self.rank[rb]:
            self.rank[ra] += 1
        return True


class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n - 1:
            return False

        dsu = DSU(n)
        for u, v in edges:
            if not dsu.union(u, v):
                return False  # cycle found
        return True


if __name__ == "__main__":
    sol = Solution()
    print("expected True, got", sol.validTree(5, [[0, 1], [0, 2], [0, 3], [1, 4]]))
    print("expected False, got", sol.validTree(5, [[0, 1], [1, 2], [2, 3], [1, 3], [1, 4]]))
    print("expected False, got", sol.validTree(4, [[0, 1], [2, 3]]))
