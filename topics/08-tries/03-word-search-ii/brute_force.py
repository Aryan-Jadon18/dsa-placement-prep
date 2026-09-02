# Independent DFS backtracking search per word — Time: O(W*m*n*4^L), Space: O(L)
from typing import List


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        rows, cols = len(board), len(board[0])

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

        return [w for w in words if exists(w)]


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
