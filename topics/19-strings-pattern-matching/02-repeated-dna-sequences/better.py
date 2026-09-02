# 2-bit-per-base rolling integer hash — Time: O(n), Space: O(n)
from collections import defaultdict
from typing import List


class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        L = 10
        n = len(s)
        if n < L:
            return []

        code = {"A": 0, "C": 1, "G": 2, "T": 3}
        mask = (1 << (2 * L)) - 1

        window_hash = 0
        for i in range(L):
            window_hash = (window_hash << 2) | code[s[i]]

        counts = defaultdict(int)
        first_text = {}  # hash -> the actual 10-letter substring it represents
        counts[window_hash] += 1
        first_text[window_hash] = s[0:L]

        result = []
        if counts[window_hash] == 2:
            result.append(first_text[window_hash])

        for i in range(L, n):
            window_hash = ((window_hash << 2) | code[s[i]]) & mask
            start = i - L + 1
            if window_hash not in first_text:
                first_text[window_hash] = s[start:start + L]
            counts[window_hash] += 1
            if counts[window_hash] == 2:
                result.append(first_text[window_hash])

        return result


if __name__ == "__main__":
    sol = Solution()
    print("Expected: ['AAAAACCCCC', 'CCCCCAAAAA'] (any order), Got:",
          sol.findRepeatedDnaSequences("AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"))
    print("Expected: ['AAAAAAAAAA'], Got:", sol.findRepeatedDnaSequences("AAAAAAAAAAAAA"))
    print("Expected: ['AAAAAAAAAA'], Got:", sol.findRepeatedDnaSequences("AAAAAAAAAAA"))
