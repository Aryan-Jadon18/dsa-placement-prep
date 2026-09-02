# Sort then scan for runs — Time: O(n log n), Space: O(1) extra
from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        arr = sorted(nums)
        best = 1
        current = 1
        for i in range(1, len(arr)):
            if arr[i] == arr[i - 1]:
                continue  # skip duplicates, streak unchanged
            if arr[i] == arr[i - 1] + 1:
                current += 1
            else:
                current = 1
            best = max(best, current)
        return best


if __name__ == "__main__":
    sol = Solution()
    print("expected 4, got", sol.longestConsecutive([100, 4, 200, 1, 3, 2]))
    print("expected 9, got", sol.longestConsecutive([0, 3, 7, 2, 5, 8, 4, 6, 0, 1]))
    print("expected 1, got", sol.longestConsecutive([1, 1, 1, 1]))
