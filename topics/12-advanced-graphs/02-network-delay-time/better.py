# Array-based Dijkstra (no heap) — Time: O(V^2), Space: O(V)
from collections import defaultdict
from typing import List


class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = defaultdict(list)
        for u, v, w in times:
            graph[u].append((v, w))

        dist = [float("inf")] * (n + 1)
        dist[k] = 0
        visited = [False] * (n + 1)

        for _ in range(n):
            u = -1
            for node in range(1, n + 1):
                if not visited[node] and (u == -1 or dist[node] < dist[u]):
                    u = node
            if u == -1 or dist[u] == float("inf"):
                break
            visited[u] = True
            for v, w in graph[u]:
                if dist[u] + w < dist[v]:
                    dist[v] = dist[u] + w

        reachable = dist[1:]
        if float("inf") in reachable:
            return -1
        return max(reachable)


if __name__ == "__main__":
    sol = Solution()
    print("expected 2, got", sol.networkDelayTime([[2, 1, 1], [2, 3, 1], [3, 4, 1]], 4, 2))
    print("expected 1, got", sol.networkDelayTime([[1, 2, 1]], 2, 1))
    print("expected -1, got", sol.networkDelayTime([[1, 2, 1]], 2, 2))
