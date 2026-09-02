# Compare each string against a representative of every existing group — Time: O(n^2 * k), Space: O(n * k)
from typing import List
from collections import Counter


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups: List[List[str]] = []
        for s in strs:
            placed = False
            for group in groups:
                if Counter(group[0]) == Counter(s):
                    group.append(s)
                    placed = True
                    break
            if not placed:
                groups.append([s])
        return groups


if __name__ == "__main__":
    sol = Solution()
    print(sol.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
    print("expected [['']], got", sol.groupAnagrams([""]))
    print("expected [['a']], got", sol.groupAnagrams(["a"]))
