# Top-down recursion + memoization via lowest-set-bit removal — Time: O(n), Space: O(n)
from functools import lru_cache
from typing import List


class Solution:
    def countBits(self, n: int) -> List[int]:
        @lru_cache(maxsize=None)
        def bits(i: int) -> int:
            if i == 0:
                return 0
            return bits(i & (i - 1)) + 1

        result = [bits(i) for i in range(n + 1)]
        bits.cache_clear()
        return result


if __name__ == "__main__":
    sol = Solution()
    print("expected [0, 1, 1], got", sol.countBits(2))
    print("expected [0, 1, 1, 2, 1, 2], got", sol.countBits(5))
    print("expected [0], got", sol.countBits(0))
