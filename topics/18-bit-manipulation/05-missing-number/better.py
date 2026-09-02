# Hash set membership check — Time: O(n), Space: O(n)
from typing import List


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        seen = set(nums)
        for i in range(len(nums) + 1):
            if i not in seen:
                return i
        return -1  # unreachable given problem guarantees


if __name__ == "__main__":
    sol = Solution()
    print("expected 2, got", sol.missingNumber([3, 0, 1]))
    print("expected 2, got", sol.missingNumber([0, 1]))
    print("expected 8, got", sol.missingNumber([9, 6, 4, 2, 3, 5, 7, 0, 1]))
