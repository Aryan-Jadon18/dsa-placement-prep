# Hierholzer's algorithm with per-node min-heaps — Time: O(E log E), Space: O(E)
import heapq
from collections import defaultdict
from typing import List


class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        graph = defaultdict(list)
        for u, v in tickets:
            heapq.heappush(graph[u], v)

        route = []
        stack = ["JFK"]
        while stack:
            airport = stack[-1]
            if graph[airport]:
                stack.append(heapq.heappop(graph[airport]))
            else:
                route.append(stack.pop())  # dead end: no more tickets out, finalize it

        return route[::-1]


if __name__ == "__main__":
    sol = Solution()
    t1 = [["MUC", "LHR"], ["JFK", "MUC"], ["SFO", "SJC"], ["LHR", "SFO"]]
    print("expected ['JFK', 'MUC', 'LHR', 'SFO', 'SJC'], got", sol.findItinerary(t1))

    t2 = [["JFK", "SFO"], ["JFK", "ATL"], ["SFO", "ATL"], ["ATL", "JFK"], ["ATL", "SFO"]]
    print("expected ['JFK', 'ATL', 'JFK', 'SFO', 'ATL', 'SFO'], got", sol.findItinerary(t2))

    t3 = [["JFK", "A"], ["A", "JFK"]]
    print("expected ['JFK', 'A', 'JFK'], got", sol.findItinerary(t3))
