# Generate all cut placements, filter for all-palindrome — Time: O(2^n * n), Space: O(2^n * n)
from typing import List


class Solution:
    def partition(self, s: str) -> List[List[str]]:
        n = len(s)
        result = []
        # Each of the n-1 gaps between characters is either a cut or not.
        for mask in range(1 << (n - 1)) if n > 1 else [0]:
            pieces = []
            piece_start = 0
            for gap in range(n - 1):
                if mask & (1 << gap):
                    pieces.append(s[piece_start:gap + 1])
                    piece_start = gap + 1
            pieces.append(s[piece_start:n])
            if all(p == p[::-1] for p in pieces):
                result.append(pieces)
        return result


if __name__ == "__main__":
    sol = Solution()
    r1 = sorted(sol.partition("aab"))
    print('expected [["a", "a", "b"], ["aa", "b"]], got', r1)

    r2 = sol.partition("a")
    print('expected [["a"]], got', r2)

    r3 = sorted(sol.partition("aba"))
    print('expected [["a", "b", "a"], ["aba"]], got', r3)
