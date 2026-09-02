# Shrinking sliding window, recompute max frequency each step — Time: O(n * 26), Space: O(26)
from collections import Counter


class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        counts = Counter()
        left = 0
        best = 0
        for right, ch in enumerate(s):
            counts[ch] += 1
            while (right - left + 1) - max(counts.values()) > k:
                counts[s[left]] -= 1
                left += 1
            best = max(best, right - left + 1)
        return best


if __name__ == "__main__":
    sol = Solution()
    print("expected 4, got", sol.characterReplacement("ABAB", 2))
    print("expected 4, got", sol.characterReplacement("AABABBA", 1))
    print("expected 4, got", sol.characterReplacement("AAAA", 0))
