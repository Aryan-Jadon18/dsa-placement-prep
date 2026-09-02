# Max-heap with lazy deletion of out-of-window entries — Time: O(n log n), Space: O(n)
import heapq
from typing import List


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        heap = []  # store (-value, index) for a max-heap via Python's min-heap
        result = []
        for i, num in enumerate(nums):
            heapq.heappush(heap, (-num, i))
            if i >= k - 1:
                while heap[0][1] <= i - k:  # top index fell out of window
                    heapq.heappop(heap)
                result.append(-heap[0][0])
        return result


if __name__ == "__main__":
    sol = Solution()
    print("expected [3,3,5,5,6,7], got", sol.maxSlidingWindow([1, 3, -1, -3, 5, 3, 6, 7], 3))
    print("expected [1], got", sol.maxSlidingWindow([1], 1))
    print("expected [11], got", sol.maxSlidingWindow([9, 11], 2))
