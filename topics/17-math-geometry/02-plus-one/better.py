# Manual carry propagation building a new reversed list — Time: O(n), Space: O(n)
from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        result = []
        carry = 1
        for digit in reversed(digits):
            total = digit + carry
            result.append(total % 10)
            carry = total // 10
        if carry:
            result.append(carry)
        result.reverse()
        return result


if __name__ == "__main__":
    sol = Solution()
    print("Expected: [1,2,4], Got:", sol.plusOne([1, 2, 3]))
    print("Expected: [4,3,2,2], Got:", sol.plusOne([4, 3, 2, 1]))
    print("Expected: [1,0,0,0], Got:", sol.plusOne([9, 9, 9]))
