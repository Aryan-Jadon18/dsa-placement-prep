# Adjacency list + BFS — Time: O(V+E), Space: O(V+E)
from collections import defaultdict, deque
from typing import List


class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        visited = [False] * n
        count = 0
        for start in range(n):
            if visited[start]:
                continue
            count += 1
            visited[start] = True
            q = deque([start])
            while q:
                node = q.popleft()
                for nxt in graph[node]:
                    if not visited[nxt]:
                        visited[nxt] = True
                        q.append(nxt)
        return count


if __name__ == "__main__":
    sol = Solution()
    print("expected 2, got", sol.countComponents(5, [[0, 1], [1, 2], [3, 4]]))
    print("expected 1, got", sol.countComponents(5, [[0, 1], [1, 2], [2, 3], [3, 4]]))
    print("expected 4, got", sol.countComponents(4, []))
