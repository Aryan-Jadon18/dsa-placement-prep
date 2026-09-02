# Plain recursion (include/exclude each element) — Time: O(2^n), Space: O(n)
from typing import List


class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2 != 0:
            return False
        target = total // 2
        n = len(nums)

        def canReach(i: int, remaining: int) -> bool:
            if remaining == 0:
                return True
            if i == n or remaining < 0:
                return False
            return canReach(i + 1, remaining - nums[i]) or canReach(i + 1, remaining)

        return canReach(0, target)


if __name__ == "__main__":
    sol = Solution()
    print("expected True, got", sol.canPartition([1, 5, 11, 5]))
    print("expected False, got", sol.canPartition([1, 2, 3, 5]))
    print("expected False, got", sol.canPartition([1, 2, 5]))
