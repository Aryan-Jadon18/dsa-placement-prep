# DP: longest chain of compatible intervals (sorted by start) — Time: O(n^2), Space: O(n)
from typing import List


class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        if not intervals:
            return 0
        ordered = sorted(intervals, key=lambda iv: iv[0])
        n = len(ordered)
        dp = [1] * n  # dp[i] = longest compatible chain ending at i

        for i in range(n):
            for j in range(i):
                if ordered[j][1] <= ordered[i][0]:
                    dp[i] = max(dp[i], dp[j] + 1)

        return n - max(dp)


if __name__ == "__main__":
    sol = Solution()
    print("Expected: 1, Got:", sol.eraseOverlapIntervals([[1, 2], [2, 3], [3, 4], [1, 3]]))
    print("Expected: 2, Got:", sol.eraseOverlapIntervals([[1, 2], [1, 2], [1, 2]]))
    print("Expected: 0, Got:", sol.eraseOverlapIntervals([[1, 2], [2, 3]]))
