# DP-precomputed palindrome table + backtracking — Time: O(n^2 + 2^n), Space: O(n^2)+output
from typing import List


class Solution:
    def partition(self, s: str) -> List[List[str]]:
        n = len(s)
        is_pal = [[False] * n for _ in range(n)]
        for i in range(n - 1, -1, -1):
            for j in range(i, n):
                if s[i] == s[j] and (j - i < 2 or is_pal[i + 1][j - 1]):
                    is_pal[i][j] = True

        result = []
        path = []

        def backtrack(start):
            if start == n:
                result.append(path[:])
                return
            for end in range(start, n):
                if is_pal[start][end]:
                    path.append(s[start:end + 1])
                    backtrack(end + 1)
                    path.pop()

        backtrack(0)
        return result


if __name__ == "__main__":
    sol = Solution()
    r1 = sorted(sol.partition("aab"))
    print('expected [["a", "a", "b"], ["aa", "b"]], got', r1)

    r2 = sol.partition("a")
    print('expected [["a"]], got', r2)

    r3 = sorted(sol.partition("aba"))
    print('expected [["a", "b", "a"], ["aba"]], got', r3)
