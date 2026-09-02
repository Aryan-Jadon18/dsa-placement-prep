# Try every speed starting from 1 upward — Time: O(max(piles) * n), Space: O(1)
import math
from typing import List


class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        k = 1
        while True:
            hours = sum(math.ceil(p / k) for p in piles)
            if hours <= h:
                return k
            k += 1


if __name__ == "__main__":
    sol = Solution()
    print("expected 4, got", sol.minEatingSpeed([3, 6, 7, 11], 8))
    print("expected 30, got", sol.minEatingSpeed([30, 11, 23, 4, 20], 5))
    print("expected 23, got", sol.minEatingSpeed([30, 11, 23, 4, 20], 6))
