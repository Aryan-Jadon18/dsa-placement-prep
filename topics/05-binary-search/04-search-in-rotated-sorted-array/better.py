# Find pivot first, then plain binary search on the correct half — Time: O(log n), Space: O(1)
from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)

        def find_pivot() -> int:
            low, high = 0, n - 1
            while low < high:
                mid = (low + high) // 2
                if nums[mid] > nums[high]:
                    low = mid + 1
                else:
                    high = mid
            return low  # index of the minimum element

        def binary_search(low: int, high: int) -> int:
            while low <= high:
                mid = (low + high) // 2
                if nums[mid] == target:
                    return mid
                elif nums[mid] < target:
                    low = mid + 1
                else:
                    high = mid - 1
            return -1

        pivot = find_pivot()
        if nums[pivot] <= target <= nums[-1]:
            return binary_search(pivot, n - 1)
        return binary_search(0, pivot - 1)


if __name__ == "__main__":
    sol = Solution()
    print("expected 4, got", sol.search([4, 5, 6, 7, 0, 1, 2], 0))
    print("expected -1, got", sol.search([4, 5, 6, 7, 0, 1, 2], 3))
    print("expected -1, got", sol.search([1], 0))
