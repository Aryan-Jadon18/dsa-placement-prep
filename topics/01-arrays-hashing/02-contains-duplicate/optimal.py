# One-pass hash set — Time: O(n), Space: O(n)
from typing import List


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        seen = set()
        for num in nums:
            if num in seen:
                return True
            seen.add(num)
        return False


if __name__ == "__main__":
    sol = Solution()
    print("expected True, got", sol.containsDuplicate([1, 2, 3, 1]))
    print("expected False, got", sol.containsDuplicate([1, 2, 3, 4]))
    print("expected True, got", sol.containsDuplicate([1, 1, 1, 3, 3, 4, 3, 2, 4, 2]))
