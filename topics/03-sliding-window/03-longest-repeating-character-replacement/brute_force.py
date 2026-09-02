# Check every substring's most-frequent-letter count — Time: O(n^2 * 26), Space: O(26)
from collections import Counter


class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        n = len(s)
        best = 0
        for i in range(n):
            counts = Counter()
            for j in range(i, n):
                counts[s[j]] += 1
                length = j - i + 1
                if length - max(counts.values()) <= k:
                    best = max(best, length)
        return best


if __name__ == "__main__":
    sol = Solution()
    print("expected 4, got", sol.characterReplacement("ABAB", 2))
    print("expected 4, got", sol.characterReplacement("AABABBA", 1))
    print("expected 4, got", sol.characterReplacement("AAAA", 0))
