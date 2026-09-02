# Plain DFS from every cell, no caching — Time: O(4^(m*n)), Space: O(m*n)
class Solution:
    def longestIncreasingPath(self, matrix: list[list[int]]) -> int:
        if not matrix or not matrix[0]:
            return 0
        rows, cols = len(matrix), len(matrix[0])
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        def dfs(r: int, c: int) -> int:
            best = 1
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols and matrix[nr][nc] > matrix[r][c]:
                    best = max(best, 1 + dfs(nr, nc))
            return best

        return max(dfs(r, c) for r in range(rows) for c in range(cols))


if __name__ == "__main__":
    sol = Solution()
    print("expected 4, got", sol.longestIncreasingPath([[9, 9, 4], [6, 6, 8], [2, 1, 1]]))
    print("expected 4, got", sol.longestIncreasingPath([[3, 4, 5], [3, 2, 6], [2, 2, 1]]))
    print("expected 1, got", sol.longestIncreasingPath([[1]]))
