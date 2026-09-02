# Single loop with a direction vector that turns at shrinking boundaries — Time: O(m*n), Space: O(1) extra
from typing import List


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix or not matrix[0]:
            return []
        rows, cols = len(matrix), len(matrix[0])
        top, bottom, left, right = 0, rows - 1, 0, cols - 1
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # right, down, left, up
        d = 0
        r = c = 0
        result = []

        for _ in range(rows * cols):
            result.append(matrix[r][c])
            dr, dc = directions[d]
            nr, nc = r + dr, c + dc

            if d == 0 and nc > right:
                top += 1
                d = 1
            elif d == 1 and nr > bottom:
                right -= 1
                d = 2
            elif d == 2 and nc < left:
                bottom -= 1
                d = 3
            elif d == 3 and nr < top:
                left += 1
                d = 0

            dr, dc = directions[d]
            r, c = r + dr, c + dc

        return result


if __name__ == "__main__":
    sol = Solution()
    print("Expected: [1,2,3,6,9,8,7,4,5], Got:",
          sol.spiralOrder([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
    print("Expected: [1,2,3,4,8,12,11,10,9,5,6,7], Got:",
          sol.spiralOrder([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]))
    print("Expected: [7], Got:", sol.spiralOrder([[7]]))
