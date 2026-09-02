# 3-color DFS cycle detection — Time: O(V+E), Space: O(V+E)
from collections import defaultdict
from typing import List

WHITE, GRAY, BLACK = 0, 1, 2  # unvisited, visiting (on stack), fully explored


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = defaultdict(list)
        for a, b in prerequisites:
            graph[b].append(a)

        color = [WHITE] * numCourses

        def has_cycle(node: int) -> bool:
            color[node] = GRAY
            for nxt in graph[node]:
                if color[nxt] == GRAY:
                    return True
                if color[nxt] == WHITE and has_cycle(nxt):
                    return True
            color[node] = BLACK
            return False

        for course in range(numCourses):
            if color[course] == WHITE and has_cycle(course):
                return False
        return True


if __name__ == "__main__":
    sol = Solution()
    print("expected True, got", sol.canFinish(2, [[1, 0]]))
    print("expected False, got", sol.canFinish(2, [[1, 0], [0, 1]]))
    print("expected True, got", sol.canFinish(4, [[1, 0], [2, 0], [3, 1], [3, 2]]))
