# Union-Find with path compression + union by rank — Time: O((V+E)*a(V)), Space: O(V)
from typing import List


class DSU:
    def __init__(self, n: int) -> None:
        self.parent = list(range(n))
        self.rank = [0] * n
        self.count = n

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
        self.count -= 1


class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        dsu = DSU(n)
        for u, v in edges:
            dsu.union(u, v)
        return dsu.count


if __name__ == "__main__":
    sol = Solution()
    print("expected 2, got", sol.countComponents(5, [[0, 1], [1, 2], [3, 4]]))
    print("expected 1, got", sol.countComponents(5, [[0, 1], [1, 2], [2, 3], [3, 4]]))
    print("expected 4, got", sol.countComponents(4, []))
