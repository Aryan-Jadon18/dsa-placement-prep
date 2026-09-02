# Linear membership scan for each candidate — Time: O(n^2), Space: O(1)
from typing import List


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        for i in range(n + 1):
            found = False
            for num in nums:
                if num == i:
                    found = True
                    break
            if not found:
                return i
        return -1  # unreachable given problem guarantees


if __name__ == "__main__":
    sol = Solution()
    print("expected 2, got", sol.missingNumber([3, 0, 1]))
    print("expected 2, got", sol.missingNumber([0, 1]))
    print("expected 8, got", sol.missingNumber([9, 6, 4, 2, 3, 5, 7, 0, 1]))
