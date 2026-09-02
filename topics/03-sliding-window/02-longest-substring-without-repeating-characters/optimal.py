# Sliding window with last-seen index map, jump left pointer — Time: O(n), Space: O(min(n,k))
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        last_seen = {}
        left = 0
        best = 0
        for right, ch in enumerate(s):
            if ch in last_seen and last_seen[ch] >= left:
                left = last_seen[ch] + 1
            last_seen[ch] = right
            best = max(best, right - left + 1)
        return best


if __name__ == "__main__":
    sol = Solution()
    print("expected 3, got", sol.lengthOfLongestSubstring("abcabcbb"))
    print("expected 1, got", sol.lengthOfLongestSubstring("bbbbb"))
    print("expected 3, got", sol.lengthOfLongestSubstring("pwwkew"))
