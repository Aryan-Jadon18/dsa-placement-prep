# Kahn's algorithm (BFS topological sort) — Time: O(V+E), Space: O(V+E)
from collections import defaultdict, deque
from typing import List


class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        indegree = [0] * numCourses
        for a, b in prerequisites:
            graph[b].append(a)
            indegree[a] += 1

        q = deque(c for c in range(numCourses) if indegree[c] == 0)
        order = []
        while q:
            course = q.popleft()
            order.append(course)
            for nxt in graph[course]:
                indegree[nxt] -= 1
                if indegree[nxt] == 0:
                    q.append(nxt)

        return order if len(order) == numCourses else []


if __name__ == "__main__":
    sol = Solution()

    def is_valid(order, numCourses, prereqs):
        if len(order) != numCourses or set(order) != set(range(numCourses)):
            return False
        pos = {c: i for i, c in enumerate(order)}
        return all(pos[b] < pos[a] for a, b in prereqs)

    r1 = sol.findOrder(2, [[1, 0]])
    print("expected valid order like [0, 1], got", r1, "valid:", is_valid(r1, 2, [[1, 0]]))

    r2 = sol.findOrder(4, [[1, 0], [2, 0], [3, 1], [3, 2]])
    print("expected valid order, got", r2, "valid:", is_valid(r2, 4, [[1, 0], [2, 0], [3, 1], [3, 2]]))

    r3 = sol.findOrder(2, [[1, 0], [0, 1]])
    print("expected [], got", r3)
