# Plain recursion — Time: O(2^n), Space: O(n)
from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)

        def helper(i: int) -> int:
            if i >= n:
                return 0
            return max(nums[i] + helper(i + 2), helper(i + 1))

        return helper(0)


if __name__ == "__main__":
    sol = Solution()
    print("expected 4, got", sol.rob([1, 2, 3, 1]))
    print("expected 12, got", sol.rob([2, 7, 9, 3, 1]))
    print("expected 5, got", sol.rob([5]))
