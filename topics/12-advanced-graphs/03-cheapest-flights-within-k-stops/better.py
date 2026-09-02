# Modified Dijkstra with (cost, node, stops) state — Time: O(E*k*log(V*k)), Space: O(V*k)
import heapq
from collections import defaultdict
from typing import List


class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        graph = defaultdict(list)
        for u, v, price in flights:
            graph[u].append((v, price))

        # best cost seen so far for reaching `node` using exactly `stops_used` stops
        best_at_stops = {}
        heap = [(0, src, 0)]  # (cost, node, stops_used)

        while heap:
            cost, node, stops_used = heapq.heappop(heap)
            if node == dst:
                return cost
            if stops_used > k:
                continue
            key = (node, stops_used)
            if key in best_at_stops and best_at_stops[key] <= cost:
                continue
            best_at_stops[key] = cost
            for nxt, price in graph[node]:
                heapq.heappush(heap, (cost + price, nxt, stops_used + 1))

        return -1


if __name__ == "__main__":
    sol = Solution()
    flights = [[0, 1, 100], [1, 2, 100], [2, 0, 100], [1, 3, 600], [2, 3, 200]]
    print("expected 700, got", sol.findCheapestPrice(4, flights, 0, 3, 1))
    print("expected 300, got", sol.findCheapestPrice(4, flights, 0, 3, 2))
    print("expected 500, got", sol.findCheapestPrice(3, [[0, 1, 100], [1, 2, 100], [0, 2, 500]], 0, 2, 0))
