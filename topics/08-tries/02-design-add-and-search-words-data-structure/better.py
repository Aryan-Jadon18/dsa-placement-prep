# Group words by length, compare within matching group — Time: search O(n'*L), Space: O(n*L)
from collections import defaultdict


class WordDictionary:
    def __init__(self):
        self.by_length = defaultdict(list)

    def addWord(self, word: str) -> None:
        self.by_length[len(word)].append(word)

    def _matches(self, word: str, pattern: str) -> bool:
        return all(p == "." or p == w for w, p in zip(word, pattern))

    def search(self, word: str) -> bool:
        candidates = self.by_length.get(len(word), [])
        return any(self._matches(w, word) for w in candidates)


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
