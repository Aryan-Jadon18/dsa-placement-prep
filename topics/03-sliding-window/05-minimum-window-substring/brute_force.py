# Check every substring against required counts — Time: O(n^2 * m), Space: O(m)
from collections import Counter


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t:
            return ""
        need = Counter(t)
        n = len(s)
        best = ""
        for i in range(n):
            for j in range(i, n):
                window = Counter(s[i:j + 1])
                if all(window[c] >= cnt for c, cnt in need.items()):
                    candidate = s[i:j + 1]
                    if best == "" or len(candidate) < len(best):
                        best = candidate
                    break  # smallest valid j for this i found, move to next i
        return best


if __name__ == "__main__":
    sol = Solution()
    print("expected BANC, got", sol.minWindow("ADOBECODEBANC", "ABC"))
    print("expected a, got", sol.minWindow("a", "a"))
    print("expected '', got", repr(sol.minWindow("a", "aa")))
