# Binary search on the answer (eating speed) — Time: O(n log(max(piles))), Space: O(1)
import math
from typing import List


class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def hours_needed(speed: int) -> int:
            return sum(math.ceil(p / speed) for p in piles)

        low, high = 1, max(piles)
        answer = high
        while low <= high:
            mid = (low + high) // 2
            if hours_needed(mid) <= h:
                answer = mid
                high = mid - 1  # try a slower (smaller) speed
            else:
                low = mid + 1  # too slow, need to eat faster
        return answer


if __name__ == "__main__":
    sol = Solution()
    print("expected 4, got", sol.minEatingSpeed([3, 6, 7, 11], 8))
    print("expected 30, got", sol.minEatingSpeed([30, 11, 23, 4, 20], 5))
    print("expected 23, got", sol.minEatingSpeed([30, 11, 23, 4, 20], 6))
