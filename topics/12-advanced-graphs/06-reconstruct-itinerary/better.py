# DFS backtracking, sorted destinations tried smallest-first — Time: O(E^2), Space: O(E)
from collections import defaultdict
from typing import List


class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        graph = defaultdict(list)
        for u, v in tickets:
            graph[u].append(v)
        for u in graph:
            graph[u].sort()  # always try lexicographically smallest destination first

        total_tickets = len(tickets)
        path = ["JFK"]

        def dfs(airport: str) -> bool:
            if len(path) == total_tickets + 1:
                return True
            for i, dest in enumerate(graph[airport]):
                if dest is None:
                    continue
                graph[airport][i] = None  # mark used
                path.append(dest)
                if dfs(dest):
                    return True
                path.pop()
                graph[airport][i] = dest  # backtrack
            return False

        dfs("JFK")
        return path


if __name__ == "__main__":
    sol = Solution()
    t1 = [["MUC", "LHR"], ["JFK", "MUC"], ["SFO", "SJC"], ["LHR", "SFO"]]
    print("expected ['JFK', 'MUC', 'LHR', 'SFO', 'SJC'], got", sol.findItinerary(t1))

    t2 = [["JFK", "SFO"], ["JFK", "ATL"], ["SFO", "ATL"], ["ATL", "JFK"], ["ATL", "SFO"]]
    print("expected ['JFK', 'ATL', 'JFK', 'SFO', 'ATL', 'SFO'], got", sol.findItinerary(t2))

    t3 = [["JFK", "A"], ["A", "JFK"]]
    print("expected ['JFK', 'A', 'JFK'], got", sol.findItinerary(t3))
