# Bottom-up tabulation via dp[i] = dp[i >> 1] + (i & 1) — Time: O(n), Space: O(n)
from typing import List


class Solution:
    def countBits(self, n: int) -> List[int]:
        dp = [0] * (n + 1)
        for i in range(1, n + 1):
            dp[i] = dp[i >> 1] + (i & 1)
        return dp


if __name__ == "__main__":
    sol = Solution()
    print("expected [0, 1, 1], got", sol.countBits(2))
    print("expected [0, 1, 1, 2, 1, 2], got", sol.countBits(5))
    print("expected [0], got", sol.countBits(0))
