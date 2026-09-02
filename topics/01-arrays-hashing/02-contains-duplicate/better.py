# Sort then scan neighbors — Time: O(n log n), Space: O(1)
from typing import List


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        arr = sorted(nums)
        for i in range(1, len(arr)):
            if arr[i] == arr[i - 1]:
                return True
        return False


if __name__ == "__main__":
    sol = Solution()
    print("expected True, got", sol.containsDuplicate([1, 2, 3, 1]))
    print("expected False, got", sol.containsDuplicate([1, 2, 3, 4]))
    print("expected True, got", sol.containsDuplicate([1, 1, 1, 3, 3, 4, 3, 2, 4, 2]))
