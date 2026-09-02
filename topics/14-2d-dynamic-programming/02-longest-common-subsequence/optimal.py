# Bottom-up tabulation, rolling 2-row array — Time: O(m*n), Space: O(min(m,n))
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        if len(text1) < len(text2):
            text1, text2 = text2, text1  # ensure text2 is the shorter one for the row
        m, n = len(text1), len(text2)

        prev = [0] * (n + 1)
        for i in range(1, m + 1):
            curr = [0] * (n + 1)
            for j in range(1, n + 1):
                if text1[i - 1] == text2[j - 1]:
                    curr[j] = prev[j - 1] + 1
                else:
                    curr[j] = max(prev[j], curr[j - 1])
            prev = curr
        return prev[n]


if __name__ == "__main__":
    sol = Solution()
    print("expected 3, got", sol.longestCommonSubsequence("abcde", "ace"))
    print("expected 3, got", sol.longestCommonSubsequence("abc", "abc"))
    print("expected 0, got", sol.longestCommonSubsequence("abc", "def"))
