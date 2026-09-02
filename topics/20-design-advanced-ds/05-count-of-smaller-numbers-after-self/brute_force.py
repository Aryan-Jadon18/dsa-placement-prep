# Nested loop, count smaller elements to the right — Time: O(n^2), Space: O(1) extra
from typing import List


class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        n = len(nums)
        counts = [0] * n
        for i in range(n):
            cnt = 0
            for j in range(i + 1, n):
                if nums[j] < nums[i]:
                    cnt += 1
            counts[i] = cnt
        return counts


if __name__ == "__main__":
    sol = Solution()
    print("Expected: [2,1,1,0], Got:", sol.countSmaller([5, 2, 6, 1]))
    print("Expected: [0], Got:", sol.countSmaller([-1]))
    print("Expected: [0,0], Got:", sol.countSmaller([-1, -1]))
