# Two pointers directly on original string, skip non-alphanumeric in place — Time: O(n), Space: O(1)
class Solution:
    def isPalindrome(self, s: str) -> bool:
        left, right = 0, len(s) - 1
        while left < right:
            while left < right and not s[left].isalnum():
                left += 1
            while left < right and not s[right].isalnum():
                right -= 1
            if s[left].lower() != s[right].lower():
                return False
            left += 1
            right -= 1
        return True


if __name__ == "__main__":
    sol = Solution()
    print("expected True, got", sol.isPalindrome("A man, a plan, a canal: Panama"))
    print("expected False, got", sol.isPalindrome("race a car"))
    print("expected True, got", sol.isPalindrome(" "))
