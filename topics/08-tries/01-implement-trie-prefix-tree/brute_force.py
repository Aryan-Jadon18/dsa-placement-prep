# Plain set of words, linear scan for prefix — Time: insert O(L), search O(1) avg, startsWith O(n*L), Space: O(total chars)


class Trie:
    def __init__(self):
        self.words = set()

    def insert(self, word: str) -> None:
        self.words.add(word)

    def search(self, word: str) -> bool:
        return word in self.words

    def startsWith(self, prefix: str) -> bool:
        return any(w.startswith(prefix) for w in self.words)


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
