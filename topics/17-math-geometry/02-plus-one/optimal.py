# In-place right-to-left carry with early exit — Time: O(n), Space: O(1) extra
from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        for i in range(len(digits) - 1, -1, -1):
            if digits[i] < 9:
                digits[i] += 1
                return digits
            digits[i] = 0  # rolls over, carry continues left

        return [1] + digits  # every digit was 9 (e.g. 999 -> 1000)


if __name__ == "__main__":
    sol = Solution()
    print("Expected: [1,2,4], Got:", sol.plusOne([1, 2, 3]))
    print("Expected: [4,3,2,2], Got:", sol.plusOne([4, 3, 2, 1]))
    print("Expected: [1,0,0,0], Got:", sol.plusOne([9, 9, 9]))
    print("Expected: [1,0], Got:", sol.plusOne([9]))
