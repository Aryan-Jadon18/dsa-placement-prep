# Nested loops — Time: O(n^2), Space: O(1)
from typing import List


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        n = len(nums)
        for i in range(n):
            for j in range(i + 1, n):
                if nums[i] == nums[j]:
                    return True
        return False


if __name__ == "__main__":
    sol = Solution()
    print("expected True, got", sol.containsDuplicate([1, 2, 3, 1]))
    print("expected False, got", sol.containsDuplicate([1, 2, 3, 4]))
    print("expected True, got", sol.containsDuplicate([1, 1, 1, 3, 3, 4, 3, 2, 4, 2]))
