# Count occurrences via nested check — Time: O(n^2), Space: O(1)
from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            count = 0
            for j in range(len(nums)):
                if nums[j] == nums[i]:
                    count += 1
            if count == 1:
                return nums[i]
        return -1  # unreachable given problem guarantees


if __name__ == "__main__":
    sol = Solution()
    print("expected 1, got", sol.singleNumber([2, 2, 1]))
    print("expected 4, got", sol.singleNumber([4, 1, 2, 1, 2]))
    print("expected 1, got", sol.singleNumber([1]))
