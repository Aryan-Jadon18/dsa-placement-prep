# Two-pointer merge, keep only the values needed for the median — Time: O(m+n), Space: O(1)
from typing import List


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        m, n = len(nums1), len(nums2)
        total = m + n
        half = total // 2

        i = j = 0
        prev = curr = 0
        for _ in range(half + 1):
            prev = curr
            if i < m and (j >= n or nums1[i] <= nums2[j]):
                curr = nums1[i]
                i += 1
            else:
                curr = nums2[j]
                j += 1

        if total % 2 == 1:
            return float(curr)
        return (prev + curr) / 2.0


if __name__ == "__main__":
    sol = Solution()
    print("expected 2.0, got", sol.findMedianSortedArrays([1, 3], [2]))
    print("expected 2.5, got", sol.findMedianSortedArrays([1, 2], [3, 4]))
    print("expected 1.0, got", sol.findMedianSortedArrays([], [1]))
