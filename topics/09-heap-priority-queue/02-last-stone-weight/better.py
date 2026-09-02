# Keep list sorted, reinsert difference with bisect.insort — Time: O(n^2) worst case, smaller constant, Space: O(n)
import bisect
from typing import List


class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        sorted_stones = sorted(stones)
        while len(sorted_stones) > 1:
            a = sorted_stones.pop()  # heaviest
            b = sorted_stones.pop()  # second heaviest
            if a != b:
                bisect.insort(sorted_stones, a - b)
        return sorted_stones[0] if sorted_stones else 0


if __name__ == "__main__":
    sol = Solution()
    print("Expected: 1  Actual:", sol.lastStoneWeight([2, 7, 4, 1, 8, 1]))
    print("Expected: 1  Actual:", sol.lastStoneWeight([1]))
    print("Expected: 0  Actual:", sol.lastStoneWeight([2, 2]))
