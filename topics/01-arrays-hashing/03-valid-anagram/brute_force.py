# Search-and-remove per character — Time: O(n^2), Space: O(n)
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        remaining = list(t)
        for ch in s:
            if ch not in remaining:
                return False
            remaining.remove(ch)  # O(n) removal, done n times
        return len(remaining) == 0


if __name__ == "__main__":
    sol = Solution()
    print("expected True, got", sol.isAnagram("anagram", "nagaram"))
    print("expected False, got", sol.isAnagram("rat", "car"))
    print("expected False, got", sol.isAnagram("aacc", "ccac"))
