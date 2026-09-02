# Frequency counting with Counter — Time: O(n), Space: O(k)
from collections import Counter


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        return Counter(s) == Counter(t)


if __name__ == "__main__":
    sol = Solution()
    print("expected True, got", sol.isAnagram("anagram", "nagaram"))
    print("expected False, got", sol.isAnagram("rat", "car"))
    print("expected False, got", sol.isAnagram("aacc", "ccac"))
