# DFS backtracking over all ticket orders, keep lexicographically smallest — Time: O(E!), Space: O(E)
from collections import Counter, defaultdict
from typing import List


class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        remaining = Counter((u, v) for u, v in tickets)
        destinations = defaultdict(set)
        for u, v in tickets:
            destinations[u].add(v)

        total_tickets = len(tickets)
        best = [None]
        path = ["JFK"]

        def dfs(airport: str) -> None:
            if len(path) == total_tickets + 1:
                if best[0] is None or path < best[0]:
                    best[0] = list(path)
                return
            for dest in destinations[airport]:  # try every order, not just sorted
                if remaining[(airport, dest)] > 0:
                    remaining[(airport, dest)] -= 1
                    path.append(dest)
                    dfs(dest)
                    path.pop()
                    remaining[(airport, dest)] += 1

        dfs("JFK")
        return best[0]


if __name__ == "__main__":
    sol = Solution()
    t1 = [["MUC", "LHR"], ["JFK", "MUC"], ["SFO", "SJC"], ["LHR", "SFO"]]
    print("expected ['JFK', 'MUC', 'LHR', 'SFO', 'SJC'], got", sol.findItinerary(t1))

    t2 = [["JFK", "SFO"], ["JFK", "ATL"], ["SFO", "ATL"], ["ATL", "JFK"], ["ATL", "SFO"]]
    print("expected ['JFK', 'ATL', 'JFK', 'SFO', 'ATL', 'SFO'], got", sol.findItinerary(t2))

    t3 = [["JFK", "A"], ["A", "JFK"]]
    print("expected ['JFK', 'A', 'JFK'], got", sol.findItinerary(t3))
