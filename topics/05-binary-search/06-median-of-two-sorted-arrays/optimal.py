# Binary search on partition point of the smaller array — Time: O(log(min(m,n))), Space: O(1)
from typing import List


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # Always binary search on the smaller array to keep partitions valid.
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        m, n = len(nums1), len(nums2)
        total = m + n
        half = (total + 1) // 2

        low, high = 0, m
        while low <= high:
            i = (low + high) // 2   # partition index in nums1
            j = half - i             # partition index in nums2

            left1 = nums1[i - 1] if i > 0 else float("-inf")
            right1 = nums1[i] if i < m else float("inf")
            left2 = nums2[j - 1] if j > 0 else float("-inf")
            right2 = nums2[j] if j < n else float("inf")

            if left1 <= right2 and left2 <= right1:
                if total % 2 == 1:
                    return float(max(left1, left2))
                return (max(left1, left2) + min(right1, right2)) / 2.0
            elif left1 > right2:
                high = i - 1  # i too big, move left
            else:
                low = i + 1   # i too small, move right

        raise ValueError("Input arrays are not sorted")


if __name__ == "__main__":
    sol = Solution()
    print("expected 2.0, got", sol.findMedianSortedArrays([1, 3], [2]))
    print("expected 2.5, got", sol.findMedianSortedArrays([1, 2], [3, 4]))
    print("expected 1.0, got", sol.findMedianSortedArrays([], [1]))
