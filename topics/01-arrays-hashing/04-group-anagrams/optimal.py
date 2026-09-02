# 26-letter count signature as hash key — Time: O(n * k), Space: O(n * k)
from typing import List
from collections import defaultdict


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        buckets = defaultdict(list)
        for s in strs:
            counts = [0] * 26
            for ch in s:
                counts[ord(ch) - ord("a")] += 1
            buckets[tuple(counts)].append(s)
        return list(buckets.values())


if __name__ == "__main__":
    sol = Solution()
    print(sol.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
    print("expected [['']], got", sol.groupAnagrams([""]))
    print("expected [['a']], got", sol.groupAnagrams(["a"]))
