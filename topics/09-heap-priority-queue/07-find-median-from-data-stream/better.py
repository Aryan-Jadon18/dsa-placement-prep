# Keep list sorted via bisect.insort — Time: addNum O(n), findMedian O(1), Space: O(n)
import bisect


class MedianFinder:
    def __init__(self):
        self.nums = []

    def addNum(self, num: int) -> None:
        bisect.insort(self.nums, num)

    def findMedian(self) -> float:
        n = len(self.nums)
        mid = n // 2
        if n % 2 == 1:
            return float(self.nums[mid])
        return (self.nums[mid - 1] + self.nums[mid]) / 2.0


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
