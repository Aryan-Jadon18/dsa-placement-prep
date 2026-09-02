# Backtracking with integer bitmasks for cols/diagonals — Time: O(n!), Space: O(n)
from typing import List


class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        result = []
        placement = []
        full_mask = (1 << n) - 1

        def backtrack(row, cols, diag1, diag2):
            if row == n:
                board = []
                for col in placement:
                    board.append("." * col + "Q" + "." * (n - col - 1))
                result.append(board)
                return
            available = full_mask & ~(cols | diag1 | diag2)
            while available:
                bit = available & -available  # lowest set bit = next candidate column
                available -= bit
                col = bit.bit_length() - 1
                placement.append(col)
                backtrack(row + 1, cols | bit, (diag1 | bit) << 1, (diag2 | bit) >> 1)
                placement.pop()

        backtrack(0, 0, 0, 0)
        return result


if __name__ == "__main__":
    sol = Solution()
    print("expected 2 solutions for n=4, got", len(sol.solveNQueens(4)))
    print("expected [['Q']], got", sol.solveNQueens(1))
    print("expected [] for n=2, got", sol.solveNQueens(2))
    print("expected [] for n=3, got", sol.solveNQueens(3))
