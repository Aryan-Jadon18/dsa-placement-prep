# Real trie with child-dict nodes — Time: O(L) per op, Space: O(total chars, shared)


class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        node = self.root
        for ch in word:
            if ch not in node.children:
                node.children[ch] = TrieNode()
            node = node.children[ch]
        node.is_end = True

    def _walk(self, s: str):
        node = self.root
        for ch in s:
            if ch not in node.children:
                return None
            node = node.children[ch]
        return node

    def search(self, word: str) -> bool:
        node = self._walk(word)
        return node is not None and node.is_end

    def startsWith(self, prefix: str) -> bool:
        return self._walk(prefix) is not None


if __name__ == "__main__":
    trie = Trie()
    trie.insert("apple")
    print("Expected: True  Actual:", trie.search("apple"))
    print("Expected: False  Actual:", trie.search("app"))
    print("Expected: True  Actual:", trie.startsWith("app"))
    trie.insert("app")
    print("Expected: True  Actual:", trie.search("app"))

    trie2 = Trie()
    trie2.insert("")
    print("Expected: True  Actual:", trie2.search(""))
