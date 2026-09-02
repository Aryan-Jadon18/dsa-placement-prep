# Min-heap capped at size k — Time: O(log k) per add, Space: O(k)
import heapq
from typing import List


class KthLargest:
    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.heap = list(nums)
        heapq.heapify(self.heap)
        while len(self.heap) > k:
            heapq.heappop(self.heap)

    def add(self, val: int) -> int:
        heapq.heappush(self.heap, val)
        if len(self.heap) > self.k:
            heapq.heappop(self.heap)
        return self.heap[0]


if __name__ == "__main__":
    kl = KthLargest(3, [4, 5, 8, 2])
    print("Expected: 4  Actual:", kl.add(3))
    print("Expected: 5  Actual:", kl.add(5))
    print("Expected: 5  Actual:", kl.add(10))
    print("Expected: 8  Actual:", kl.add(9))

    kl2 = KthLargest(1, [])
    print("Expected: -3  Actual:", kl2.add(-3))
