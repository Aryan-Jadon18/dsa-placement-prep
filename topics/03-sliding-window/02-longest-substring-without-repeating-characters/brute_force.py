# Check every substring for uniqueness — Time: O(n^3), Space: O(min(n,k))
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        best = 0
        for i in range(n):
            for j in range(i, n):
                window = s[i:j + 1]
                if len(set(window)) == len(window):
                    best = max(best, len(window))
        return best


if __name__ == "__main__":
    sol = Solution()
    print("expected 3, got", sol.lengthOfLongestSubstring("abcabcbb"))
    print("expected 1, got", sol.lengthOfLongestSubstring("bbbbb"))
    print("expected 3, got", sol.lengthOfLongestSubstring("pwwkew"))
