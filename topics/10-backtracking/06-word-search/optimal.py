# DFS marking board cells in place, no extra structure — Time: O(m*n*4^L), Space: O(L)
from typing import List


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows, cols = len(board), len(board[0])

        def dfs(r, c, i):
            if i == len(word):
                return True
            if r < 0 or r >= rows or c < 0 or c >= cols:
                return False
            if board[r][c] != word[i]:
                return False
            original = board[r][c]
            board[r][c] = "#"  # sentinel: can never match a real letter
            found = (
                dfs(r + 1, c, i + 1)
                or dfs(r - 1, c, i + 1)
                or dfs(r, c + 1, i + 1)
                or dfs(r, c - 1, i + 1)
            )
            board[r][c] = original
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
