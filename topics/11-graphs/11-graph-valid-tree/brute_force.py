# Edge-count check + adjacency matrix DFS for connectivity — Time: O(n^2), Space: O(n^2)
from typing import List


class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n - 1:
            return False
        if n == 1:
            return True

        matrix = [[False] * n for _ in range(n)]
        for u, v in edges:
            matrix[u][v] = True
            matrix[v][u] = True

        visited = [False] * n

        def dfs(node: int) -> None:
            visited[node] = True
            for nxt in range(n):
                if matrix[node][nxt] and not visited[nxt]:
                    dfs(nxt)

        dfs(0)
        return all(visited)


if __name__ == "__main__":
    sol = Solution()
    print("expected True, got", sol.validTree(5, [[0, 1], [0, 2], [0, 3], [1, 4]]))
    print("expected False, got", sol.validTree(5, [[0, 1], [1, 2], [2, 3], [1, 3], [1, 4]]))
    print("expected False, got", sol.validTree(4, [[0, 1], [2, 3]]))
