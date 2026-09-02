# Sort and compare — Time: O(n log n), Space: O(n)
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        return sorted(s) == sorted(t)


if __name__ == "__main__":
    sol = Solution()
    print("expected True, got", sol.isAnagram("anagram", "nagaram"))
    print("expected False, got", sol.isAnagram("rat", "car"))
    print("expected False, got", sol.isAnagram("aacc", "ccac"))
