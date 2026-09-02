# Two heaps + lazy deletion — Time: O(n log k), Space: O(k)
import heapq
from collections import defaultdict
from typing import List


class Solution:
    def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:
        small: List[int] = []  # max-heap (values negated) - the smaller half
        large: List[int] = []  # min-heap - the larger half
        delayed = defaultdict(int)  # value -> count of pending lazy deletions
        small_size = large_size = 0  # effective sizes, excluding pending deletions

        def prune(heap: List[int]) -> None:
            # a heap's top only needs cleaning when IT is the stale element
            sign = -1 if heap is small else 1
            while heap and delayed[sign * heap[0]] > 0:
                delayed[sign * heap[0]] -= 1
                heapq.heappop(heap)

        def rebalance() -> None:
            nonlocal small_size, large_size
            if small_size > large_size + 1:
                heapq.heappush(large, -small[0])
                heapq.heappop(small)
                small_size -= 1
                large_size += 1
                prune(small)
            elif small_size < large_size:
                heapq.heappush(small, -large[0])
                heapq.heappop(large)
                large_size -= 1
                small_size += 1
                prune(large)

        def add(num: int) -> None:
            nonlocal small_size, large_size
            if not small or num <= -small[0]:
                heapq.heappush(small, -num)
                small_size += 1
            else:
                heapq.heappush(large, num)
                large_size += 1
            rebalance()

        def remove(num: int) -> None:
            nonlocal small_size, large_size
            delayed[num] += 1
            if num <= -small[0]:
                small_size -= 1
                if num == -small[0]:
                    prune(small)
            else:
                large_size -= 1
                if large and num == large[0]:
                    prune(large)
            rebalance()

        def get_median() -> float:
            if k % 2:
                return float(-small[0])
            return (-small[0] + large[0]) / 2.0

        result = []
        for i in range(k):
            add(nums[i])
        result.append(get_median())

        for i in range(k, len(nums)):
            add(nums[i])
            remove(nums[i - k])
            result.append(get_median())

        return result


if __name__ == "__main__":
    sol = Solution()
    print("Expected: [1.0, -1.0, -1.0, 3.0, 5.0, 6.0], Got:",
          sol.medianSlidingWindow([1, 3, -1, -3, 5, 3, 6, 7], 3))
    print("Expected: [2.0, 3.0, 3.0, 3.0, 2.0, 3.0, 2.0], Got:",
          sol.medianSlidingWindow([1, 2, 3, 4, 2, 3, 1, 4, 2], 3))
    print("Expected: [1.5], Got:", sol.medianSlidingWindow([1, 2], 2))
