# Sorted list maintained incrementally with bisect — Time: O(n*k), Space: O(k)
import bisect
from typing import List


class Solution:
    def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:
        window = sorted(nums[:k])
        result = [self._median(window, k)]

        for i in range(k, len(nums)):
            outgoing = nums[i - k]
            pos = bisect.bisect_left(window, outgoing)
            window.pop(pos)  # O(k) shift

            bisect.insort(window, nums[i])  # O(k) shift

            result.append(self._median(window, k))

        return result

    @staticmethod
    def _median(window: List[int], k: int) -> float:
        if k % 2 == 1:
            return float(window[k // 2])
        return (window[k // 2 - 1] + window[k // 2]) / 2.0


if __name__ == "__main__":
    sol = Solution()
    print("Expected: [1.0, -1.0, -1.0, 3.0, 5.0, 6.0], Got:",
          sol.medianSlidingWindow([1, 3, -1, -3, 5, 3, 6, 7], 3))
    print("Expected: [2.0, 3.0, 3.0, 3.0, 2.0, 3.0, 2.0], Got:",
          sol.medianSlidingWindow([1, 2, 3, 4, 2, 3, 1, 4, 2], 3))
    print("Expected: [1.5], Got:", sol.medianSlidingWindow([1, 2], 2))
