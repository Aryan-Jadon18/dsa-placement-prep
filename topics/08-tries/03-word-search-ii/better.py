# Skip words whose letters aren't all present on the board, then DFS per word — Time: O(W*m*n*4^L), smaller constant, Space: O(L+26)
from typing import List
from collections import Counter


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        rows, cols = len(board), len(board[0])
        board_letters = Counter(ch for row in board for ch in row)

        def exists(word: str) -> bool:
            visited = set()

            def dfs(r, c, i):
                if i == len(word):
                    return True
                if (r < 0 or r >= rows or c < 0 or c >= cols
                        or (r, c) in visited or board[r][c] != word[i]):
                    return False
                visited.add((r, c))
                found = (dfs(r + 1, c, i + 1) or dfs(r - 1, c, i + 1)
                         or dfs(r, c + 1, i + 1) or dfs(r, c - 1, i + 1))
                visited.remove((r, c))
                return found

            for r in range(rows):
                for c in range(cols):
                    if dfs(r, c, 0):
                        return True
            return False

        result = []
        for w in words:
            needed = Counter(w)
            # quick reject: word needs more of some letter than the board has
            if any(needed[ch] > board_letters.get(ch, 0) for ch in needed):
                continue
            if exists(w):
                result.append(w)
        return result


if __name__ == "__main__":
    sol = Solution()

    board1 = [["o", "a", "a", "n"], ["e", "t", "a", "e"],
              ["i", "h", "k", "r"], ["i", "f", "l", "v"]]
    words1 = ["oath", "pea", "eat", "rain"]
    print("Expected: {'oath', 'eat'}  Actual:", set(sol.findWords(board1, words1)))

    board2 = [["a", "b"], ["c", "d"]]
    words2 = ["abcb"]
    print("Expected: []  Actual:", sol.findWords(board2, words2))

    board3 = [["a"]]
    words3 = ["a"]
    print("Expected: ['a']  Actual:", sol.findWords(board3, words3))
