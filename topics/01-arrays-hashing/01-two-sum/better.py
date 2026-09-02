# Sort + two pointers, map back to original indices — Time: O(n log n), Space: O(n)
from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        indexed = sorted(range(len(nums)), key=lambda i: nums[i])
        lo, hi = 0, len(indexed) - 1
        while lo < hi:
            s = nums[indexed[lo]] + nums[indexed[hi]]
            if s == target:
                return sorted([indexed[lo], indexed[hi]])
            if s < target:
                lo += 1
            else:
                hi -= 1
        return []


if __name__ == "__main__":
    sol = Solution()
    print("expected [0, 1], got", sol.twoSum([2, 7, 11, 15], 9))
    print("expected [1, 2], got", sol.twoSum([3, 2, 4], 6))
    print("expected [0, 1], got", sol.twoSum([3, 3], 6))
