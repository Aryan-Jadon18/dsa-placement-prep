# DFS with one shared visited set, mark/unmark — Time: O(m*n*4^L), Space: O(L)
from typing import List


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows, cols = len(board), len(board[0])
        visited = set()

        def dfs(r, c, i):
            if i == len(word):
                return True
            if r < 0 or r >= rows or c < 0 or c >= cols:
                return False
            if (r, c) in visited or board[r][c] != word[i]:
                return False
            visited.add((r, c))
            found = any(
                dfs(r + dr, c + dc, i + 1)
                for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1))
            )
            visited.remove((r, c))
            return found

        for r in range(rows):
            for c in range(cols):
                if dfs(r, c, 0):
                    return True
        return False


if __name__ == "__main__":
    sol = Solution()
    board = [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]]
    print("expected True, got", sol.exist([row[:] for row in board], "ABCCED"))
    print("expected True, got", sol.exist([row[:] for row in board], "SEE"))
    print("expected False, got", sol.exist([row[:] for row in board], "ABCB"))
