# Sliding window, validity re-checked via frequency comparison — Time: O(n * 26), Space: O(52)
from collections import Counter


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t:
            return ""
        need = Counter(t)
        window = Counter()
        left = 0
        best_len = float("inf")
        best_start = 0

        def is_valid():
            return all(window[c] >= cnt for c, cnt in need.items())

        for right, ch in enumerate(s):
            window[ch] += 1
            while is_valid():
                if right - left + 1 < best_len:
                    best_len = right - left + 1
                    best_start = left
                window[s[left]] -= 1
                left += 1

        return "" if best_len == float("inf") else s[best_start:best_start + best_len]


if __name__ == "__main__":
    sol = Solution()
    print("expected BANC, got", sol.minWindow("ADOBECODEBANC", "ABC"))
    print("expected a, got", sol.minWindow("a", "a"))
    print("expected '', got", repr(sol.minWindow("a", "aa")))
