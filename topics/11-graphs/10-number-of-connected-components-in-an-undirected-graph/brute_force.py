# Adjacency matrix + DFS — Time: O(n^2 + E), Space: O(n^2)
from typing import List


class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
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

        count = 0
        for node in range(n):
            if not visited[node]:
                count += 1
                dfs(node)
        return count


if __name__ == "__main__":
    sol = Solution()
    print("expected 2, got", sol.countComponents(5, [[0, 1], [1, 2], [3, 4]]))
    print("expected 1, got", sol.countComponents(5, [[0, 1], [1, 2], [2, 3], [3, 4]]))
    print("expected 4, got", sol.countComponents(4, []))
