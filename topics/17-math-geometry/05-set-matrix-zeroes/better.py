# Two boolean marker arrays for rows/cols — Time: O(m*n), Space: O(m+n)
from typing import List


class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        rows, cols = len(matrix), len(matrix[0])
        zero_rows = [False] * rows
        zero_cols = [False] * cols

        for r in range(rows):
            for c in range(cols):
                if matrix[r][c] == 0:
                    zero_rows[r] = True
                    zero_cols[c] = True

        for r in range(rows):
            for c in range(cols):
                if zero_rows[r] or zero_cols[c]:
                    matrix[r][c] = 0


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
