# Hash map counting — Time: O(n), Space: O(n)
from collections import Counter
from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        counts = Counter(nums)
        for num, c in counts.items():
            if c == 1:
                return num
        return -1  # unreachable given problem guarantees


if __name__ == "__main__":
    sol = Solution()
    print("expected 1, got", sol.singleNumber([2, 2, 1]))
    print("expected 4, got", sol.singleNumber([4, 1, 2, 1, 2]))
    print("expected 1, got", sol.singleNumber([1]))
