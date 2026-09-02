# Naive Union-Find, no path compression / no union by rank — Time: O(n^2) worst case, Space: O(n)
from typing import List


class DSU:
    def __init__(self, n: int) -> None:
        self.parent = list(range(n + 1))

    def find(self, x: int) -> int:
        while self.parent[x] != x:  # no path compression
            x = self.parent[x]
        return x

    def union(self, a: int, b: int) -> bool:
        ra, rb = self.find(a), self.find(b)
        if ra == rb:
            return False
        self.parent[rb] = ra  # always attach arbitrarily, no rank/size
        return True


class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        dsu = DSU(n)
        for u, v in edges:
            if not dsu.union(u, v):
                return [u, v]
        return []


if __name__ == "__main__":
    sol = Solution()
    print("expected [2, 3], got", sol.findRedundantConnection([[1, 2], [1, 3], [2, 3]]))
    print("expected [1, 4], got", sol.findRedundantConnection([[1, 2], [2, 3], [3, 4], [1, 4], [1, 5]]))
    print("expected [3, 4], got", sol.findRedundantConnection([[1, 2], [1, 3], [2, 4], [3, 4]]))
