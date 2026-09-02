# Bottom-up tabulation, rolling 2-row array — Time: O(m*n), Space: O(n)
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        m, n = len(s), len(p)

        prev = [False] * (n + 1)
        prev[0] = True
        for j in range(1, n + 1):
            if p[j - 1] == "*" and j >= 2:
                prev[j] = prev[j - 2]

        for i in range(1, m + 1):
            curr = [False] * (n + 1)
            for j in range(1, n + 1):
                pc = p[j - 1]
                if pc != "*":
                    curr[j] = prev[j - 1] and (pc == s[i - 1] or pc == ".")
                else:
                    zero_occurrences = curr[j - 2] if j >= 2 else False
                    one_more = j >= 2 and prev[j] and (p[j - 2] == s[i - 1] or p[j - 2] == ".")
                    curr[j] = zero_occurrences or one_more
            prev = curr

        return prev[n]


if __name__ == "__main__":
    sol = Solution()
    print("expected True, got", sol.isMatch("aa", "a*"))
    print("expected True, got", sol.isMatch("ab", ".*"))
    print("expected False, got", sol.isMatch("mississippi", "mis*is*p*."))
