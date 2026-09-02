# Per-edge BFS connectivity check against edges added so far — Time: O(n^2), Space: O(n)
from collections import defaultdict, deque
from typing import List


class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        graph = defaultdict(list)

        def connected(u: int, v: int) -> bool:
            if u not in graph:
                return False
            visited = {u}
            q = deque([u])
            while q:
                cur = q.popleft()
                if cur == v:
                    return True
                for nxt in graph[cur]:
                    if nxt not in visited:
                        visited.add(nxt)
                        q.append(nxt)
            return False

        for u, v in edges:
            if connected(u, v):
                return [u, v]
            graph[u].append(v)
            graph[v].append(u)
        return []


if __name__ == "__main__":
    sol = Solution()
    print("expected [2, 3], got", sol.findRedundantConnection([[1, 2], [1, 3], [2, 3]]))
    print("expected [1, 4], got", sol.findRedundantConnection([[1, 2], [2, 3], [3, 4], [1, 4], [1, 5]]))
    print("expected [3, 4], got", sol.findRedundantConnection([[1, 2], [1, 3], [2, 4], [3, 4]]))
