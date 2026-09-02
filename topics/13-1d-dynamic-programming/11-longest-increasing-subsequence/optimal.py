# Patience sorting with binary search, hand-written (no bisect) — Time: O(n log n), Space: O(n)
from typing import List


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        tails: List[int] = []  # tails[k] = smallest tail value of an increasing subsequence of length k+1

        def lowerBound(target: int) -> int:
            lo, hi = 0, len(tails)
            while lo < hi:
                mid = (lo + hi) // 2
                if tails[mid] < target:
                    lo = mid + 1
                else:
                    hi = mid
            return lo

        for num in nums:
            pos = lowerBound(num)
            if pos == len(tails):
                tails.append(num)
            else:
                tails[pos] = num
        return len(tails)


if __name__ == "__main__":
    sol = Solution()
    print("expected 4, got", sol.lengthOfLIS([10, 9, 2, 5, 3, 7, 101, 18]))
    print("expected 4, got", sol.lengthOfLIS([0, 1, 0, 3, 2, 3]))
    print("expected 1, got", sol.lengthOfLIS([7, 7, 7, 7]))
