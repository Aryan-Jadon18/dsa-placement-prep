# Build cleaned string, compare to its reverse — Time: O(n), Space: O(n)
class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleaned = [ch.lower() for ch in s if ch.isalnum()]
        cleaned_str = "".join(cleaned)
        return cleaned_str == cleaned_str[::-1]


if __name__ == "__main__":
    sol = Solution()
    print("expected True, got", sol.isPalindrome("A man, a plan, a canal: Panama"))
    print("expected False, got", sol.isPalindrome("race a car"))
    print("expected True, got", sol.isPalindrome(" "))
