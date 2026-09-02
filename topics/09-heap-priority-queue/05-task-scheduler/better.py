# Max-heap simulation, processed in rounds of size n+1 — Time: O(t log 26), Space: O(26)
import heapq
from typing import List
from collections import Counter


class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counts = Counter(tasks)
        heap = [-c for c in counts.values()]
        heapq.heapify(heap)

        time = 0
        while heap:
            batch = []  # tasks used in this round of size n+1
            for _ in range(n + 1):
                if heap:
                    batch.append(-heapq.heappop(heap))
            for cnt in batch:
                if cnt - 1 > 0:
                    heapq.heappush(heap, -(cnt - 1))
            # full round unless this was the very last (partial) round with no leftovers
            time += (n + 1) if heap else len(batch)

        return time


if __name__ == "__main__":
    sol = Solution()
    print("Expected: 8  Actual:", sol.leastInterval(["A", "A", "A", "B", "B", "B"], 2))
    print("Expected: 6  Actual:", sol.leastInterval(["A", "A", "A", "B", "B", "B"], 0))
    print("Expected: 16  Actual:", sol.leastInterval(
        ["A", "A", "A", "A", "A", "A", "B", "C", "D", "E", "F", "G"], 2))
