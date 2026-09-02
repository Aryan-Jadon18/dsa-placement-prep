# Sliding window that only slides (never shrinks below best size) — Time: O(n), Space: O(26)
from collections import defaultdict


class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        counts = defaultdict(int)
        left = 0
        max_freq = 0
        for right, ch in enumerate(s):
            counts[ch] += 1
            max_freq = max(max_freq, counts[ch])
            if (right - left + 1) - max_freq > k:
                counts[s[left]] -= 1
                left += 1
        return len(s) - left


if __name__ == "__main__":
    sol = Solution()
    print("expected 4, got", sol.characterReplacement("ABAB", 2))
    print("expected 4, got", sol.characterReplacement("AABABBA", 1))
    print("expected 4, got", sol.characterReplacement("AAAA", 0))
