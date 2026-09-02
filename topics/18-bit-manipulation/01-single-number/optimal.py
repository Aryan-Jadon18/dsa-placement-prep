# XOR accumulator — Time: O(n), Space: O(1)
from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        result = 0
        for num in nums:
            result ^= num
        return result


if __name__ == "__main__":
    sol = Solution()
    print("expected 1, got", sol.singleNumber([2, 2, 1]))
    print("expected 4, got", sol.singleNumber([4, 1, 2, 1, 2]))
    print("expected 1, got", sol.singleNumber([1]))
