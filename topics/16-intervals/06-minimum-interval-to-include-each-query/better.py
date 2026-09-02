# Sort both lists, sweep with a pointer, linear scan of "active" intervals — Time: O(q*n) worst case, Space: O(n)
from typing import List


class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        ordered_intervals = sorted(intervals, key=lambda iv: iv[0])
        indexed_queries = sorted(range(len(queries)), key=lambda i: queries[i])

        answers = [-1] * len(queries)
        active: List[List[int]] = []  # intervals whose left <= current query
        ptr = 0
        n = len(ordered_intervals)

        for qi in indexed_queries:
            q = queries[qi]
            while ptr < n and ordered_intervals[ptr][0] <= q:
                active.append(ordered_intervals[ptr])
                ptr += 1

            best = -1
            for left, right in active:
                if right >= q:
                    size = right - left + 1
                    if best == -1 or size < best:
                        best = size
            answers[qi] = best

        return answers


if __name__ == "__main__":
    sol = Solution()
    print("Expected: [3,3,1,4], Got:",
          sol.minInterval([[1, 4], [2, 4], [3, 6], [4, 4]], [2, 3, 4, 5]))
    print("Expected: [2,-1,4,6], Got:",
          sol.minInterval([[2, 3], [2, 5], [1, 8], [20, 25]], [2, 19, 5, 22]))
    print("Expected: [10], Got:", sol.minInterval([[1, 10]], [5]))
