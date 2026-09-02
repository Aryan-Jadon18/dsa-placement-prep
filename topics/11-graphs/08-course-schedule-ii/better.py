# DFS postorder topological sort with cycle detection — Time: O(V+E), Space: O(V+E)
from collections import defaultdict
from typing import List

WHITE, GRAY, BLACK = 0, 1, 2


class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        for a, b in prerequisites:
            graph[b].append(a)  # b -> a

        color = [WHITE] * numCourses
        postorder = []
        has_cycle = False

        def dfs(node: int) -> None:
            nonlocal has_cycle
            color[node] = GRAY
            for nxt in graph[node]:
                if color[nxt] == GRAY:
                    has_cycle = True
                    return
                if color[nxt] == WHITE:
                    dfs(nxt)
                    if has_cycle:
                        return
            color[node] = BLACK
            postorder.append(node)

        for course in range(numCourses):
            if color[course] == WHITE:
                dfs(course)
            if has_cycle:
                return []

        return postorder[::-1]


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
