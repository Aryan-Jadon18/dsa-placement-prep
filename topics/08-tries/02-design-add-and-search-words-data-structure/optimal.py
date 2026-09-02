# Trie + DFS backtracking for '.' wildcards — Time: O(L) no dots, O(26^d * L) worst case, Space: O(total chars)


class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False


class WordDictionary:
    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        node = self.root
        for ch in word:
            if ch not in node.children:
                node.children[ch] = TrieNode()
            node = node.children[ch]
        node.is_end = True

    def search(self, word: str) -> bool:
        def dfs(node: TrieNode, i: int) -> bool:
            if i == len(word):
                return node.is_end
            ch = word[i]
            if ch == ".":
                return any(dfs(child, i + 1) for child in node.children.values())
            child = node.children.get(ch)
            return child is not None and dfs(child, i + 1)

        return dfs(self.root, 0)


if __name__ == "__main__":
    wd = WordDictionary()
    wd.addWord("bad")
    wd.addWord("dad")
    wd.addWord("mad")
    print("Expected: False  Actual:", wd.search("pad"))
    print("Expected: True  Actual:", wd.search("bad"))
    print("Expected: True  Actual:", wd.search(".ad"))
    print("Expected: True  Actual:", wd.search("b.."))

    wd2 = WordDictionary()
    wd2.addWord("a")
    print("Expected: True  Actual:", wd2.search("."))

    wd3 = WordDictionary()
    wd3.addWord("ab")
    print("Expected: False  Actual:", wd3.search("a"))
