# New matrix via direct rotation formula, then copy back — Time: O(n^2), Space: O(n^2)
from typing import List


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        n = len(matrix)
        rotated = [[0] * n for _ in range(n)]
        for r in range(n):
            for c in range(n):
                rotated[c][n - 1 - r] = matrix[r][c]

        for r in range(n):
            for c in range(n):
                matrix[r][c] = rotated[r][c]


if __name__ == "__main__":
    sol = Solution()
    m1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    sol.rotate(m1)
    print("Expected: [[7,4,1],[8,5,2],[9,6,3]], Got:", m1)

    m2 = [[5, 1, 9, 11], [2, 4, 8, 10], [13, 3, 6, 7], [15, 14, 12, 16]]
    sol.rotate(m2)
    print("Expected: [[15,13,2,5],[14,3,4,1],[12,6,8,9],[16,7,10,11]], Got:", m2)

    m3 = [[1]]
    sol.rotate(m3)
    print("Expected: [[1]], Got:", m3)
