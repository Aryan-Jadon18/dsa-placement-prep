# "Burst last" recursion memoized on (left, right) — Time: O(n^3), Space: O(n^2)
from functools import lru_cache


class Solution:
    def maxCoins(self, nums: list[int]) -> int:
        vals = [1] + nums + [1]
        n = len(vals)

        @lru_cache(maxsize=None)
        def solve(left: int, right: int) -> int:
            if right - left <= 1:
                return 0
            best = 0
            for k in range(left + 1, right):
                gain = vals[left] * vals[k] * vals[right] + solve(left, k) + solve(k, right)
                best = max(best, gain)
            return best

        result = solve(0, n - 1)
        solve.cache_clear()
        return result


if __name__ == "__main__":
    sol = Solution()
    print("expected 167, got", sol.maxCoins([3, 1, 5, 8]))
    print("expected 10, got", sol.maxCoins([1, 5]))
    print("expected 7, got", sol.maxCoins([7]))
