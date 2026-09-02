# Four shrinking boundaries, one loop per side — Time: O(m*n), Space: O(1) extra
from typing import List


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix or not matrix[0]:
            return []
        top, bottom = 0, len(matrix) - 1
        left, right = 0, len(matrix[0]) - 1
        result = []

        while top <= bottom and left <= right:
            for c in range(left, right + 1):
                result.append(matrix[top][c])
            top += 1

            for r in range(top, bottom + 1):
                result.append(matrix[r][right])
            right -= 1

            if top <= bottom:
                for c in range(right, left - 1, -1):
                    result.append(matrix[bottom][c])
                bottom -= 1

            if left <= right:
                for r in range(bottom, top - 1, -1):
                    result.append(matrix[r][left])
                left += 1

        return result


if __name__ == "__main__":
    sol = Solution()
    print("Expected: [1,2,3,6,9,8,7,4,5], Got:",
          sol.spiralOrder([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
    print("Expected: [1,2,3,4,8,12,11,10,9,5,6,7], Got:",
          sol.spiralOrder([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]))
    print("Expected: [7], Got:", sol.spiralOrder([[7]]))
