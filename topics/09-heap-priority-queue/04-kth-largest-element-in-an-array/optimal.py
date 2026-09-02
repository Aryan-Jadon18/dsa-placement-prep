# Quickselect (random pivot partitioning) — Time: O(n) average, O(n^2) worst, Space: O(1) extra
import random
from typing import List


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums = list(nums)
        target_idx = len(nums) - k  # k-th largest = index (n-k) in ascending order

        def partition(lo, hi, pivot_idx):
            pivot_val = nums[pivot_idx]
            nums[pivot_idx], nums[hi] = nums[hi], nums[pivot_idx]
            store = lo
            for i in range(lo, hi):
                if nums[i] < pivot_val:
                    nums[i], nums[store] = nums[store], nums[i]
                    store += 1
            nums[store], nums[hi] = nums[hi], nums[store]
            return store

        lo, hi = 0, len(nums) - 1
        while lo < hi:
            pivot_idx = random.randint(lo, hi)
            pos = partition(lo, hi, pivot_idx)
            if pos == target_idx:
                break
            elif pos < target_idx:
                lo = pos + 1
            else:
                hi = pos - 1

        return nums[target_idx]


if __name__ == "__main__":
    sol = Solution()
    print("Expected: 5  Actual:", sol.findKthLargest([3, 2, 1, 5, 6, 4], 2))
    print("Expected: 4  Actual:", sol.findKthLargest([3, 2, 3, 1, 2, 4, 5, 5, 6], 4))
    print("Expected: 1  Actual:", sol.findKthLargest([1], 1))
