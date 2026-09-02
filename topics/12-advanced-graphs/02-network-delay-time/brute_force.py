# Bellman-Ford — Time: O(V*E), Space: O(V)
from typing import List


class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        dist = [float("inf")] * (n + 1)
        dist[k] = 0

        for _ in range(n - 1):
            updated = False
            for u, v, w in times:
                if dist[u] + w < dist[v]:
                    dist[v] = dist[u] + w
                    updated = True
            if not updated:
                break

        reachable = dist[1:]
        if float("inf") in reachable:
            return -1
        return max(reachable)


if __name__ == "__main__":
    sol = Solution()
    print("expected 2, got", sol.networkDelayTime([[2, 1, 1], [2, 3, 1], [3, 4, 1]], 4, 2))
    print("expected 1, got", sol.networkDelayTime([[1, 2, 1]], 2, 1))
    print("expected -1, got", sol.networkDelayTime([[1, 2, 1]], 2, 2))
