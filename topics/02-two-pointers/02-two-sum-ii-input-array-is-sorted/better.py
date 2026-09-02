# One-pass hash map (ignores sortedness, uses extra space) — Time: O(n), Space: O(n)
from typing import List


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        seen = {}  # value -> 1-indexed position
        for i, num in enumerate(numbers):
            complement = target - num
            if complement in seen:
                return [seen[complement], i + 1]
            seen[num] = i + 1
        return []


if __name__ == "__main__":
    sol = Solution()
    print("expected [1, 2], got", sol.twoSum([2, 7, 11, 15], 9))
    print("expected [1, 3], got", sol.twoSum([2, 3, 4], 6))
    print("expected [1, 2], got", sol.twoSum([-1, 0], -1))
