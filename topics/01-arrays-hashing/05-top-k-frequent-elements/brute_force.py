# Repeatedly scan frequency map for current max — Time: O(n * d), Space: O(n)
from typing import List
from collections import Counter


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = Counter(nums)
        remaining = dict(freq)
        result = []
        for _ in range(k):
            best_val = max(remaining, key=remaining.get)
            result.append(best_val)
            del remaining[best_val]
        return result


if __name__ == "__main__":
    sol = Solution()
    print("expected {1,2}, got", set(sol.topKFrequent([1, 1, 1, 2, 2, 3], 2)))
    print("expected [1], got", sol.topKFrequent([1], 1))
    print("expected {4,6}, got", set(sol.topKFrequent([4, 4, 4, 6, 6, 7], 2)))
