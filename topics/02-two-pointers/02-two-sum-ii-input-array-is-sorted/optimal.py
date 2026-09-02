# Two pointers exploiting sorted order — Time: O(n), Space: O(1)
from typing import List


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left, right = 0, len(numbers) - 1
        while left < right:
            total = numbers[left] + numbers[right]
            if total == target:
                return [left + 1, right + 1]
            if total < target:
                left += 1
            else:
                right -= 1
        return []


if __name__ == "__main__":
    sol = Solution()
    print("expected [1, 2], got", sol.twoSum([2, 7, 11, 15], 9))
    print("expected [1, 3], got", sol.twoSum([2, 3, 4], 6))
    print("expected [1, 2], got", sol.twoSum([-1, 0], -1))
