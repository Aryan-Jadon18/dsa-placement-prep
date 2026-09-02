# Per-node self-reachability DFS, no shared memo — Time: O(V*(V+E)), Space: O(V+E)
from collections import defaultdict
from typing import List


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = defaultdict(list)
        for a, b in prerequisites:
            graph[b].append(a)  # b -> a: finish b before a

        def can_reach_self(start: int) -> bool:
            visited = set()
            stack = list(graph[start])
            while stack:
                node = stack.pop()
                if node == start:
                    return True
                if node in visited:
                    continue
                visited.add(node)
                stack.extend(graph[node])
            return False

        for course in range(numCourses):
            if can_reach_self(course):
                return False
        return True


if __name__ == "__main__":
    sol = Solution()
    print("expected True, got", sol.canFinish(2, [[1, 0]]))
    print("expected False, got", sol.canFinish(2, [[1, 0], [0, 1]]))
    print("expected True, got", sol.canFinish(4, [[1, 0], [2, 0], [3, 1], [3, 2]]))
