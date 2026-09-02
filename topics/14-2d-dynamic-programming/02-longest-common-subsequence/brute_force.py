# Plain recursion over both strings — Time: O(2^(m+n)), Space: O(m+n)
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        def lcs(i: int, j: int) -> int:
            if i == len(text1) or j == len(text2):
                return 0
            if text1[i] == text2[j]:
                return 1 + lcs(i + 1, j + 1)
            return max(lcs(i + 1, j), lcs(i, j + 1))

        return lcs(0, 0)


if __name__ == "__main__":
    sol = Solution()
    print("expected 3, got", sol.longestCommonSubsequence("abcde", "ace"))
    print("expected 3, got", sol.longestCommonSubsequence("abc", "abc"))
    print("expected 0, got", sol.longestCommonSubsequence("abc", "def"))
