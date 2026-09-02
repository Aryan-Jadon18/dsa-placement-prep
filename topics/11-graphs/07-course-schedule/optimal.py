# Kahn's algorithm (BFS topological sort) — Time: O(V+E), Space: O(V+E)
from collections import defaultdict, deque
from typing import List


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = defaultdict(list)
        indegree = [0] * numCourses
        for a, b in prerequisites:
            graph[b].append(a)
            indegree[a] += 1

        q = deque(c for c in range(numCourses) if indegree[c] == 0)
        completed = 0
        while q:
            course = q.popleft()
            completed += 1
            for nxt in graph[course]:
                indegree[nxt] -= 1
                if indegree[nxt] == 0:
                    q.append(nxt)

        return completed == numCourses


if __name__ == "__main__":
    sol = Solution()
    print("expected True, got", sol.canFinish(2, [[1, 0]]))
    print("expected False, got", sol.canFinish(2, [[1, 0], [0, 1]]))
    print("expected True, got", sol.canFinish(4, [[1, 0], [2, 0], [3, 1], [3, 2]]))
