# Sliding window with have/need counters, O(1) validity check — Time: O(n + m), Space: O(52)
from collections import Counter


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t:
            return ""
        need = Counter(t)
        need_distinct = len(need)
        window = Counter()
        have = 0
        left = 0
        best_len = float("inf")
        best_start = 0

        for right, ch in enumerate(s):
            window[ch] += 1
            if ch in need and window[ch] == need[ch]:
                have += 1

            while have == need_distinct:
                if right - left + 1 < best_len:
                    best_len = right - left + 1
                    best_start = left
                left_ch = s[left]
                window[left_ch] -= 1
                if left_ch in need and window[left_ch] == need[left_ch] - 1:
                    have -= 1
                left += 1

        return "" if best_len == float("inf") else s[best_start:best_start + best_len]


if __name__ == "__main__":
    sol = Solution()
    print("expected BANC, got", sol.minWindow("ADOBECODEBANC", "ABC"))
    print("expected a, got", sol.minWindow("a", "a"))
    print("expected '', got", repr(sol.minWindow("a", "aa")))
