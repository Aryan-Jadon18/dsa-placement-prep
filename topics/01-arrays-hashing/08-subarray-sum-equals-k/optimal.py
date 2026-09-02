# Running prefix sum + hash map of prefix-sum frequencies — Time: O(n), Space: O(n)
from typing import List
from collections import defaultdict


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix_counts = defaultdict(int)
        prefix_counts[0] = 1  # empty prefix, needed for subarrays starting at index 0
        running = 0
        count = 0
        for num in nums:
            running += num
            count += prefix_counts[running - k]
            prefix_counts[running] += 1
        return count


if __name__ == "__main__":
    sol = Solution()
    print("expected 2, got", sol.subarraySum([1, 1, 1], 2))
    print("expected 2, got", sol.subarraySum([1, 2, 3], 3))
    print("expected 3, got", sol.subarraySum([1, -1, 0], 0))
