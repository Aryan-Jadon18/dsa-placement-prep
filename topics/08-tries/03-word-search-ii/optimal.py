# Trie of all words + single DFS pass over the board — Time: O(m*n*4^L) + trie build, Space: O(sum word lengths + m*n)
from typing import List


class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = None  # full word stored at the terminal node, or None


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root = TrieNode()
        for w in words:
            node = root
            for ch in w:
                node = node.children.setdefault(ch, TrieNode())
            node.word = w

        rows, cols = len(board), len(board[0])
        result = []

        def dfs(r, c, node):
            ch = board[r][c]
            child = node.children.get(ch)
            if child is None:
                return

            if child.word is not None:
                result.append(child.word)
                child.word = None  # avoid duplicate reporting

            board[r][c] = "#"  # mark visited in place
            for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols and board[nr][nc] != "#":
                    dfs(nr, nc, child)
            board[r][c] = ch

            if not child.children:  # prune dead trie branches
                node.children.pop(ch, None)

        for r in range(rows):
            for c in range(cols):
                dfs(r, c, root)

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
