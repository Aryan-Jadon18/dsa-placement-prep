# Count then full sort by frequency — Time: O(n + d log d), Space: O(n)
from typing import List
from collections import Counter


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = Counter(nums)
        ordered = sorted(freq.items(), key=lambda pair: pair[1], reverse=True)
        return [val for val, _ in ordered[:k]]


if __name__ == "__main__":
    sol = Solution()
    print("expected {1,2}, got", set(sol.topKFrequent([1, 1, 1, 2, 2, 3], 2)))
    print("expected [1], got", sol.topKFrequent([1], 1))
    print("expected {4,6}, got", set(sol.topKFrequent([4, 4, 4, 6, 6, 7], 2)))
