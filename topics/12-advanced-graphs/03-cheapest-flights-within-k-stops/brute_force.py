# DFS/backtracking over all paths within the stop limit — Time: O(V^k), Space: O(k)
from collections import defaultdict
from typing import List


class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        graph = defaultdict(list)
        for u, v, price in flights:
            graph[u].append((v, price))

        best = [float("inf")]

        def dfs(node: int, cost: int, stops_left: int) -> None:
            if cost >= best[0]:
                return  # prune: can't possibly improve
            if node == dst:
                best[0] = cost
                return
            if stops_left < 0:
                return
            for nxt, price in graph[node]:
                dfs(nxt, cost + price, stops_left - 1)

        dfs(src, 0, k)
        return best[0] if best[0] != float("inf") else -1


if __name__ == "__main__":
    sol = Solution()
    flights = [[0, 1, 100], [1, 2, 100], [2, 0, 100], [1, 3, 600], [2, 3, 200]]
    print("expected 700, got", sol.findCheapestPrice(4, flights, 0, 3, 1))
    print("expected 400, got", sol.findCheapestPrice(4, flights, 0, 3, 2))
    print("expected 500, got", sol.findCheapestPrice(3, [[0, 1, 100], [1, 2, 100], [0, 2, 500]], 0, 2, 0))
