# Sort + min-heap of (size, right), expire stale intervals as queries grow — Time: O((n+q) log n), Space: O(n+q)
import heapq
from typing import List


class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        ordered_intervals = sorted(intervals, key=lambda iv: iv[0])
        indexed_queries = sorted(range(len(queries)), key=lambda i: queries[i])

        answers = [-1] * len(queries)
        heap: List[List[int]] = []  # (size, right)
        ptr = 0
        n = len(ordered_intervals)

        for qi in indexed_queries:
            q = queries[qi]

            while ptr < n and ordered_intervals[ptr][0] <= q:
                left, right = ordered_intervals[ptr]
                heapq.heappush(heap, [right - left + 1, right])
                ptr += 1

            while heap and heap[0][1] < q:  # expired: can never cover this or later queries
                heapq.heappop(heap)

            if heap:
                answers[qi] = heap[0][0]

        return answers


if __name__ == "__main__":
    sol = Solution()
    print("Expected: [3,3,1,4], Got:",
          sol.minInterval([[1, 4], [2, 4], [3, 6], [4, 4]], [2, 3, 4, 5]))
    print("Expected: [2,-1,4,6], Got:",
          sol.minInterval([[2, 3], [2, 5], [1, 8], [20, 25]], [2, 19, 5, 22]))
    print("Expected: [10], Got:", sol.minInterval([[1, 10]], [5]))
