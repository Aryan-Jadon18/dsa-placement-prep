# Simulated walker with a visited grid, turning when blocked — Time: O(m*n), Space: O(m*n)
from typing import List


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix or not matrix[0]:
            return []
        rows, cols = len(matrix), len(matrix[0])
        visited = [[False] * cols for _ in range(rows)]
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # right, down, left, up

        result = []
        r = c = d = 0
        for _ in range(rows * cols):
            result.append(matrix[r][c])
            visited[r][c] = True
            dr, dc = directions[d]
            nr, nc = r + dr, c + dc
            if not (0 <= nr < rows and 0 <= nc < cols) or visited[nr][nc]:
                d = (d + 1) % 4
                dr, dc = directions[d]
                nr, nc = r + dr, c + dc
            r, c = nr, nc

        return result


if __name__ == "__main__":
    sol = Solution()
    print("Expected: [1,2,3,6,9,8,7,4,5], Got:",
          sol.spiralOrder([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
    print("Expected: [1,2,3,4,8,12,11,10,9,5,6,7], Got:",
          sol.spiralOrder([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]))
    print("Expected: [7], Got:", sol.spiralOrder([[7]]))
