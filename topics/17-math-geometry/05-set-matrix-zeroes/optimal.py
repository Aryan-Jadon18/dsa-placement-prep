# Use first row/column as marker storage — Time: O(m*n), Space: O(1) extra
from typing import List


class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        rows, cols = len(matrix), len(matrix[0])
        first_row_has_zero = any(matrix[0][c] == 0 for c in range(cols))
        first_col_has_zero = any(matrix[r][0] == 0 for r in range(rows))

        for r in range(1, rows):
            for c in range(1, cols):
                if matrix[r][c] == 0:
                    matrix[r][0] = 0
                    matrix[0][c] = 0

        for r in range(1, rows):
            for c in range(1, cols):
                if matrix[r][0] == 0 or matrix[0][c] == 0:
                    matrix[r][c] = 0

        if first_row_has_zero:
            for c in range(cols):
                matrix[0][c] = 0

        if first_col_has_zero:
            for r in range(rows):
                matrix[r][0] = 0


if __name__ == "__main__":
    sol = Solution()
    m1 = [[1, 1, 1], [1, 0, 1], [1, 1, 1]]
    sol.setZeroes(m1)
    print("Expected: [[1,0,1],[0,0,0],[1,0,1]], Got:", m1)

    m2 = [[0, 1, 2, 0], [3, 4, 5, 2], [1, 3, 1, 5]]
    sol.setZeroes(m2)
    print("Expected: [[0,0,0,0],[0,4,5,0],[0,3,1,0]], Got:", m2)

    m3 = [[1, 2], [3, 4]]
    sol.setZeroes(m3)
    print("Expected: [[1,2],[3,4]], Got:", m3)
