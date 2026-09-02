# Nested loop, recompute product for each index — Time: O(n^2), Space: O(1) extra
from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        answer = [1] * n
        for i in range(n):
            prod = 1
            for j in range(n):
                if j != i:
                    prod *= nums[j]
            answer[i] = prod
        return answer


if __name__ == "__main__":
    sol = Solution()
    print("expected [24,12,8,6], got", sol.productExceptSelf([1, 2, 3, 4]))
    print("expected [0,0,9,0,0], got", sol.productExceptSelf([-1, 1, 0, -3, 3]))
    print("expected [3,2], got", sol.productExceptSelf([2, 3]))
