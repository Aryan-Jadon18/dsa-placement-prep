# Two heaps: max-heap for low half, min-heap for high half — Time: addNum O(log n), findMedian O(1), Space: O(n)
import heapq


class MedianFinder:
    def __init__(self):
        self.low = []   # max-heap (negated) — smaller half
        self.high = []  # min-heap — larger half

    def addNum(self, num: int) -> None:
        heapq.heappush(self.low, -num)
        # ensure everything in low <= everything in high
        heapq.heappush(self.high, -heapq.heappop(self.low))
        # keep low with equal size or exactly one more than high
        if len(self.high) > len(self.low):
            heapq.heappush(self.low, -heapq.heappop(self.high))

    def findMedian(self) -> float:
        if len(self.low) > len(self.high):
            return float(-self.low[0])
        return (-self.low[0] + self.high[0]) / 2.0


if __name__ == "__main__":
    mf = MedianFinder()
    mf.addNum(1)
    mf.addNum(2)
    print("Expected: 1.5  Actual:", mf.findMedian())
    mf.addNum(3)
    print("Expected: 2  Actual:", mf.findMedian())

    mf2 = MedianFinder()
    mf2.addNum(-1)
    print("Expected: -1  Actual:", mf2.findMedian())

    mf3 = MedianFinder()
    for x in [5, 2, 8, 1]:
        mf3.addNum(x)
    print("Expected: 3.5  Actual:", mf3.findMedian())
