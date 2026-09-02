# Slice every 10-letter window, count with a hash map — Time: O(n*L), Space: O(n*L)
from collections import defaultdict
from typing import List


class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        L = 10
        n = len(s)
        if n < L:
            return []

        counts = defaultdict(int)
        for i in range(n - L + 1):
            window = s[i:i + L]
            counts[window] += 1

        return [seq for seq, cnt in counts.items() if cnt >= 2]


if __name__ == "__main__":
    sol = Solution()
    print("Expected: ['AAAAACCCCC', 'CCCCCAAAAA'] (any order), Got:",
          sol.findRepeatedDnaSequences("AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"))
    print("Expected: ['AAAAAAAAAA'], Got:", sol.findRepeatedDnaSequences("AAAAAAAAAAAAA"))
    print("Expected: ['AAAAAAAAAA'], Got:", sol.findRepeatedDnaSequences("AAAAAAAAAAA"))
