# Iterative DP over cells sorted by value (DAG topological order) — Time: O(m*n log(m*n)), Space: O(m*n)
class Solution:
    def longestIncreasingPath(self, matrix: list[list[int]]) -> int:
        if not matrix or not matrix[0]:
            return 0
        rows, cols = len(matrix), len(matrix[0])
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        cells = sorted(
            ((r, c) for r in range(rows) for c in range(cols)),
            key=lambda rc: matrix[rc[0]][rc[1]],
            reverse=True,  # process largest values first
        )

        dp = [[1] * cols for _ in range(rows)]
        for r, c in cells:
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols and matrix[nr][nc] > matrix[r][c]:
                    dp[r][c] = max(dp[r][c], 1 + dp[nr][nc])

        return max(max(row) for row in dp)


if __name__ == "__main__":
    sol = Solution()
    print("expected 4, got", sol.longestIncreasingPath([[9, 9, 4], [6, 6, 8], [2, 1, 1]]))
    print("expected 4, got", sol.longestIncreasingPath([[3, 4, 5], [3, 2, 6], [2, 2, 1]]))
    print("expected 1, got", sol.longestIncreasingPath([[1]]))
