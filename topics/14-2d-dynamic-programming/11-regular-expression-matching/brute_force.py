# Plain recursion over (i, j) with explicit star handling — Time: O(2^(m+n)), Space: O(m+n)
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        m, n = len(s), len(p)

        def dfs(i: int, j: int) -> bool:
            if j == n:
                return i == m
            first_match = i < m and (p[j] == s[i] or p[j] == ".")
            if j + 1 < n and p[j + 1] == "*":
                return dfs(i, j + 2) or (first_match and dfs(i + 1, j))
            return first_match and dfs(i + 1, j + 1)

        return dfs(0, 0)


if __name__ == "__main__":
    sol = Solution()
    print("expected True, got", sol.isMatch("aa", "a*"))
    print("expected True, got", sol.isMatch("ab", ".*"))
    print("expected False, got", sol.isMatch("mississippi", "mis*is*p*."))
