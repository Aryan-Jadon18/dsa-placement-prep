# Max-heap via negation — Time: O(n log n), Space: O(n)
import heapq
from typing import List


class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = [-w for w in stones]
        heapq.heapify(heap)

        while len(heap) > 1:
            a = -heapq.heappop(heap)  # heaviest
            b = -heapq.heappop(heap)  # second heaviest
            if a != b:
                heapq.heappush(heap, -(a - b))

        return -heap[0] if heap else 0


if __name__ == "__main__":
    sol = Solution()
    print("Expected: 1  Actual:", sol.lastStoneWeight([2, 7, 4, 1, 8, 1]))
    print("Expected: 1  Actual:", sol.lastStoneWeight([1]))
    print("Expected: 0  Actual:", sol.lastStoneWeight([2, 2]))
