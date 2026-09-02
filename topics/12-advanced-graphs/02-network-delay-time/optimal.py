# Dijkstra's algorithm with a min-heap — Time: O(E log V), Space: O(V+E)
import heapq
from collections import defaultdict
from typing import List


class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = defaultdict(list)
        for u, v, w in times:
            graph[u].append((v, w))

        dist = {}
        heap = [(0, k)]
        while heap:
            d, u = heapq.heappop(heap)
            if u in dist:
                continue  # stale entry, already finalized with a better distance
            dist[u] = d
            for v, w in graph[u]:
                if v not in dist:
                    heapq.heappush(heap, (d + w, v))

        if len(dist) != n:
            return -1
        return max(dist.values())


if __name__ == "__main__":
    sol = Solution()
    print("expected 2, got", sol.networkDelayTime([[2, 1, 1], [2, 3, 1], [3, 4, 1]], 4, 2))
    print("expected 1, got", sol.networkDelayTime([[1, 2, 1]], 2, 1))
    print("expected -1, got", sol.networkDelayTime([[1, 2, 1]], 2, 2))
