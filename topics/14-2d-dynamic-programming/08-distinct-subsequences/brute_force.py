# Plain recursion, skip-or-use each character of s — Time: O(2^len(s)), Space: O(len(s))
class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        m, n = len(s), len(t)

        def dfs(i: int, j: int) -> int:
            if j == n:
                return 1
            if i == m:
                return 0
            ways = dfs(i + 1, j)  # skip s[i]
            if s[i] == t[j]:
                ways += dfs(i + 1, j + 1)  # use s[i] to match t[j]
            return ways

        return dfs(0, 0)


if __name__ == "__main__":
    sol = Solution()
    print("expected 3, got", sol.numDistinct("rabbbit", "rabbit"))
    print("expected 5, got", sol.numDistinct("babgbag", "bag"))
    print("expected 0, got", sol.numDistinct("abc", "abcd"))
