# Bellman-Ford limited to k+1 rounds — Time: O(k*E), Space: O(V)
from typing import List


class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        dist = [float("inf")] * n
        dist[src] = 0

        for _ in range(k + 1):
            new_dist = dist[:]  # read from previous round only, prevents chaining hops
            for u, v, price in flights:
                if dist[u] != float("inf") and dist[u] + price < new_dist[v]:
                    new_dist[v] = dist[u] + price
            dist = new_dist

        return dist[dst] if dist[dst] != float("inf") else -1


if __name__ == "__main__":
    sol = Solution()
    flights = [[0, 1, 100], [1, 2, 100], [2, 0, 100], [1, 3, 600], [2, 3, 200]]
    print("expected 700, got", sol.findCheapestPrice(4, flights, 0, 3, 1))
    print("expected 400, got", sol.findCheapestPrice(4, flights, 0, 3, 2))
    print("expected 500, got", sol.findCheapestPrice(3, [[0, 1, 100], [1, 2, 100], [0, 2, 500]], 0, 2, 0))
