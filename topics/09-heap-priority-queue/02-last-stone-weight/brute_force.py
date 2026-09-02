# Scan for the two largest every round — Time: O(n^2), Space: O(n)
from typing import List


class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = list(stones)
        while len(stones) > 1:
            stones.sort()
            a = stones.pop()  # heaviest
            b = stones.pop()  # second heaviest
            if a != b:
                stones.append(a - b)
        return stones[0] if stones else 0


if __name__ == "__main__":
    sol = Solution()
    print("Expected: 1  Actual:", sol.lastStoneWeight([2, 7, 4, 1, 8, 1]))
    print("Expected: 1  Actual:", sol.lastStoneWeight([1]))
    print("Expected: 0  Actual:", sol.lastStoneWeight([2, 2]))
