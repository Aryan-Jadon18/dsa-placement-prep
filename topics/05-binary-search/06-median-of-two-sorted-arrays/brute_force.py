# Merge and sort, then index the middle — Time: O((m+n) log(m+n)), Space: O(m+n)
from typing import List


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        merged = sorted(nums1 + nums2)
        n = len(merged)
        mid = n // 2
        if n % 2 == 1:
            return float(merged[mid])
        return (merged[mid - 1] + merged[mid]) / 2.0


if __name__ == "__main__":
    sol = Solution()
    print("expected 2.0, got", sol.findMedianSortedArrays([1, 3], [2]))
    print("expected 2.5, got", sol.findMedianSortedArrays([1, 2], [3, 4]))
    print("expected 1.0, got", sol.findMedianSortedArrays([], [1]))
