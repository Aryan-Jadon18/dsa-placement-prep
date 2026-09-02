# Bottom-up tabulation on two linear sub-cases, O(1) space — Time: O(n), Space: O(1)
from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]

        def linearRob(arr: List[int]) -> int:
            prev2, prev1 = 0, 0
            for num in arr:
                prev2, prev1 = prev1, max(prev1, prev2 + num)
            return prev1

        return max(linearRob(nums[:-1]), linearRob(nums[1:]))


if __name__ == "__main__":
    sol = Solution()
    print("expected 3, got", sol.rob([2, 3, 2]))
    print("expected 4, got", sol.rob([1, 2, 3, 1]))
    print("expected 3, got", sol.rob([1, 2, 3]))
