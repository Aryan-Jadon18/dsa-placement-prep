# Repeated full-scan for satisfied courses — Time: O(V^2 + V*E), Space: O(V+E)
from collections import defaultdict
from typing import List


class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        prereq_of = defaultdict(set)
        for a, b in prerequisites:
            prereq_of[a].add(b)

        taken = [False] * numCourses
        order = []

        for _ in range(numCourses):
            placed_this_round = False
            for course in range(numCourses):
                if taken[course]:
                    continue
                if prereq_of[course].issubset(set(order)):
                    taken[course] = True
                    order.append(course)
                    placed_this_round = True
                    break  # rescan from scratch next round (deliberately naive)
            if not placed_this_round:
                return []

        return order


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
