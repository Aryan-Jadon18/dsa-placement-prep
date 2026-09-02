# Backtracking, re-scan all placed queens for every check — Time: O(n^(n+1)), Space: O(n)
from typing import List


class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        result = []
        placement = []  # placement[row] = col of the queen in that row

        def conflicts(row, col):
            for prev_row, prev_col in enumerate(placement):
                if prev_col == col:
                    return True
                if abs(prev_row - row) == abs(prev_col - col):
                    return True
            return False

        def backtrack(row):
            if row == n:
                board = []
                for col in placement:
                    board.append("." * col + "Q" + "." * (n - col - 1))
                result.append(board)
                return
            for col in range(n):
                if not conflicts(row, col):
                    placement.append(col)
                    backtrack(row + 1)
                    placement.pop()

        backtrack(0)
        return result


if __name__ == "__main__":
    sol = Solution()
    print("expected 2 solutions for n=4, got", len(sol.solveNQueens(4)))
    print("expected [['Q']], got", sol.solveNQueens(1))
    print("expected [] for n=2, got", sol.solveNQueens(2))
    print("expected [] for n=3, got", sol.solveNQueens(3))
