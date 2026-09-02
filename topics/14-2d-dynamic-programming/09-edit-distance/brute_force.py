# Plain recursion trying replace/delete/insert — Time: O(3^(m+n)), Space: O(m+n)
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m, n = len(word1), len(word2)

        def dfs(i: int, j: int) -> int:
            if i == m:
                return n - j  # insert the rest of word2
            if j == n:
                return m - i  # delete the rest of word1
            if word1[i] == word2[j]:
                return dfs(i + 1, j + 1)
            replace = dfs(i + 1, j + 1)
            delete = dfs(i + 1, j)
            insert = dfs(i, j + 1)
            return 1 + min(replace, delete, insert)

        return dfs(0, 0)


if __name__ == "__main__":
    sol = Solution()
    print("expected 3, got", sol.minDistance("horse", "ros"))
    print("expected 5, got", sol.minDistance("intention", "execution"))
    print("expected 3, got", sol.minDistance("", "abc"))
