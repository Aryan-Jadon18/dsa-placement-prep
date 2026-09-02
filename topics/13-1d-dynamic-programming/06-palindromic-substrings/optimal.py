# Expand around center, O(1) extra space — Time: O(n^2), Space: O(1)
class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        count = 0

        def expand(left: int, right: int) -> int:
            local = 0
            while left >= 0 and right < n and s[left] == s[right]:
                local += 1
                left -= 1
                right += 1
            return local

        for i in range(n):
            count += expand(i, i)       # odd-length palindromes centered at i
            count += expand(i, i + 1)   # even-length palindromes centered between i, i+1
        return count


if __name__ == "__main__":
    sol = Solution()
    print("expected 3, got", sol.countSubstrings("abc"))
    print("expected 6, got", sol.countSubstrings("aaa"))
    print("expected 4, got", sol.countSubstrings("aba"))
