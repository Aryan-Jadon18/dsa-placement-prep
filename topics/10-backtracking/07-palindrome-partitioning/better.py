# Backtracking, prune non-palindromic prefixes early — Time: O(2^n * n), Space: O(n)+output
from typing import List


class Solution:
    def partition(self, s: str) -> List[List[str]]:
        n = len(s)
        result = []
        path = []

        def is_palindrome(sub):
            return sub == sub[::-1]

        def backtrack(start):
            if start == n:
                result.append(path[:])
                return
            for end in range(start + 1, n + 1):
                piece = s[start:end]
                if is_palindrome(piece):
                    path.append(piece)
                    backtrack(end)
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
