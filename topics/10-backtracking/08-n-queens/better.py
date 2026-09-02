# Backtracking with three tracking sets (cols, diag1, diag2) — Time: O(n!), Space: O(n)
from typing import List


class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        result = []
        placement = []
        cols = set()
        diag1 = set()  # row - col
        diag2 = set()  # row + col

        def backtrack(row):
            if row == n:
                board = []
                for col in placement:
                    board.append("." * col + "Q" + "." * (n - col - 1))
                result.append(board)
                return
            for col in range(n):
                if col in cols or (row - col) in diag1 or (row + col) in diag2:
                    continue
                cols.add(col)
                diag1.add(row - col)
                diag2.add(row + col)
                placement.append(col)

                backtrack(row + 1)

                placement.pop()
                cols.remove(col)
                diag1.remove(row - col)
                diag2.remove(row + col)

        backtrack(0)
        return result


if __name__ == "__main__":
    sol = Solution()
    print("expected 2 solutions for n=4, got", len(sol.solveNQueens(4)))
    print("expected [['Q']], got", sol.solveNQueens(1))
    print("expected [] for n=2, got", sol.solveNQueens(2))
    print("expected [] for n=3, got", sol.solveNQueens(3))
