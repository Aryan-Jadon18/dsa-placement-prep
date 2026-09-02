# Bucket sort by frequency — Time: O(n), Space: O(n)
from typing import List
from collections import Counter


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = Counter(nums)
        n = len(nums)
        buckets = [[] for _ in range(n + 1)]  # index = frequency
        for val, cnt in freq.items():
            buckets[cnt].append(val)

        result = []
        for cnt in range(n, 0, -1):
            for val in buckets[cnt]:
                result.append(val)
                if len(result) == k:
                    return result
        return result

        # Alternative optimal-ish: heapq.nlargest(k, freq.keys(), key=freq.get) -> O(n log k)


if __name__ == "__main__":
    sol = Solution()
    print("expected {1,2}, got", set(sol.topKFrequent([1, 1, 1, 2, 2, 3], 2)))
    print("expected [1], got", sol.topKFrequent([1], 1))
    print("expected {4,6}, got", set(sol.topKFrequent([4, 4, 4, 6, 6, 7], 2)))
