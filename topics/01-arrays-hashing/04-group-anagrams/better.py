# Sorted-string as hash key — Time: O(n * k log k), Space: O(n * k)
from typing import List
from collections import defaultdict


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        buckets = defaultdict(list)
        for s in strs:
            key = "".join(sorted(s))
            buckets[key].append(s)
        return list(buckets.values())


if __name__ == "__main__":
    sol = Solution()
    print(sol.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
    print("expected [['']], got", sol.groupAnagrams([""]))
    print("expected [['a']], got", sol.groupAnagrams(["a"]))
