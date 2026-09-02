# Independently count bits of every number — Time: O(n log n), Space: O(n)
from typing import List


class Solution:
    def countBits(self, n: int) -> List[int]:
        def popcount(x: int) -> int:
            count = 0
            while x:
                x &= x - 1
                count += 1
            return count

        return [popcount(i) for i in range(n + 1)]


if __name__ == "__main__":
    sol = Solution()
    print("expected [0, 1, 1], got", sol.countBits(2))
    print("expected [0, 1, 1, 2, 1, 2], got", sol.countBits(5))
    print("expected [0], got", sol.countBits(0))
