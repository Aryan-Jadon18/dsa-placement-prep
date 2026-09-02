# Clean once, then two pointers on the cleaned string — Time: O(n), Space: O(n)
class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleaned = "".join(ch.lower() for ch in s if ch.isalnum())
        left, right = 0, len(cleaned) - 1
        while left < right:
            if cleaned[left] != cleaned[right]:
                return False
            left += 1
            right -= 1
        return True


if __name__ == "__main__":
    sol = Solution()
    print("expected True, got", sol.isPalindrome("A man, a plan, a canal: Panama"))
    print("expected False, got", sol.isPalindrome("race a car"))
    print("expected True, got", sol.isPalindrome(" "))
