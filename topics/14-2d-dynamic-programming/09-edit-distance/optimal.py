# Bottom-up tabulation, rolling 2-row array — Time: O(m*n), Space: O(min(m,n))
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        if len(word1) < len(word2):
            word1, word2 = word2, word1  # keep word2 (the row) shorter
        m, n = len(word1), len(word2)

        prev = list(range(n + 1))
        for i in range(1, m + 1):
            curr = [i] + [0] * n
            for j in range(1, n + 1):
                if word1[i - 1] == word2[j - 1]:
                    curr[j] = prev[j - 1]
                else:
                    curr[j] = 1 + min(prev[j - 1], prev[j], curr[j - 1])
            prev = curr
        return prev[n]


if __name__ == "__main__":
    sol = Solution()
    print("expected 3, got", sol.minDistance("horse", "ros"))
    print("expected 5, got", sol.minDistance("intention", "execution"))
    print("expected 3, got", sol.minDistance("", "abc"))
