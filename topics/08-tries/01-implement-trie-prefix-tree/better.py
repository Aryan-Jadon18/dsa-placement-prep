# Word set + precomputed prefix set — Time: insert O(L^2), search O(1) avg, startsWith O(1) avg, Space: O(n*L^2)


class Trie:
    def __init__(self):
        self.words = set()
        self.prefixes = set()

    def insert(self, word: str) -> None:
        self.words.add(word)
        for i in range(len(word) + 1):
            self.prefixes.add(word[:i])

    def search(self, word: str) -> bool:
        return word in self.words

    def startsWith(self, prefix: str) -> bool:
        return prefix in self.prefixes


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
