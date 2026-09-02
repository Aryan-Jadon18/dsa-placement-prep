# Nested loops ignoring sorted order — Time: O(n^2), Space: O(1)
from typing import List


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        n = len(numbers)
        for i in range(n):
            for j in range(i + 1, n):
                if numbers[i] + numbers[j] == target:
                    return [i + 1, j + 1]
        return []


if __name__ == "__main__":
    sol = Solution()
    print("expected [1, 2], got", sol.twoSum([2, 7, 11, 15], 9))
    print("expected [1, 3], got", sol.twoSum([2, 3, 4], 6))
    print("expected [1, 2], got", sol.twoSum([-1, 0], -1))
