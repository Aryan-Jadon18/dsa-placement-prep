# Bottom-up rolling max/min ending here — Time: O(n), Space: O(1)
from typing import List


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        result = nums[0]
        curMax, curMin = nums[0], nums[0]
        for num in nums[1:]:
            candidates = (num, num * curMax, num * curMin)
            curMax, curMin = max(candidates), min(candidates)
            result = max(result, curMax)
        return result


if __name__ == "__main__":
    sol = Solution()
    print("expected 6, got", sol.maxProduct([2, 3, -2, 4]))
    print("expected 0, got", sol.maxProduct([-2, 0, -1]))
    print("expected 24, got", sol.maxProduct([-2, 3, -4]))
