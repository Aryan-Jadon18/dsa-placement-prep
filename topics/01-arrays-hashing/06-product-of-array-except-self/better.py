# Separate prefix and suffix product arrays — Time: O(n), Space: O(n)
from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        prefix = [1] * n
        suffix = [1] * n

        for i in range(1, n):
            prefix[i] = prefix[i - 1] * nums[i - 1]

        for i in range(n - 2, -1, -1):
            suffix[i] = suffix[i + 1] * nums[i + 1]

        return [prefix[i] * suffix[i] for i in range(n)]


if __name__ == "__main__":
    sol = Solution()
    print("expected [24,12,8,6], got", sol.productExceptSelf([1, 2, 3, 4]))
    print("expected [0,0,9,0,0], got", sol.productExceptSelf([-1, 1, 0, -3, 3]))
    print("expected [3,2], got", sol.productExceptSelf([2, 3]))
