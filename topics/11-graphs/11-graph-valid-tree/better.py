# Edge-count check + adjacency list DFS with parent tracking — Time: O(V+E), Space: O(V+E)
from collections import defaultdict
from typing import List


class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n - 1:
            return False
        if n == 1:
            return True

        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        visited = set()

        def dfs(node: int, parent: int) -> bool:
            visited.add(node)
            for nxt in graph[node]:
                if nxt == parent:
                    continue  # skip the edge we just came from
                if nxt in visited:
                    return False  # found a cycle
                if not dfs(nxt, node):
                    return False
            return True

        if not dfs(0, -1):
            return False
        return len(visited) == n


if __name__ == "__main__":
    sol = Solution()
    print("expected True, got", sol.validTree(5, [[0, 1], [0, 2], [0, 3], [1, 4]]))
    print("expected False, got", sol.validTree(5, [[0, 1], [1, 2], [2, 3], [1, 3], [1, 4]]))
    print("expected False, got", sol.validTree(4, [[0, 1], [2, 3]]))
