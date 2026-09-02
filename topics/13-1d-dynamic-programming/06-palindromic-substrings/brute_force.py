# Check every substring — Time: O(n^3), Space: O(1) extra
class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        count = 0
        for i in range(n):
            for j in range(i, n):
                sub = s[i:j + 1]
                if sub == sub[::-1]:
                    count += 1
        return count


if __name__ == "__main__":
    sol = Solution()
    print("expected 3, got", sol.countSubstrings("abc"))
    print("expected 6, got", sol.countSubstrings("aaa"))
    print("expected 4, got", sol.countSubstrings("aba"))
