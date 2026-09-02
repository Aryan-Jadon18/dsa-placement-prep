# BFS generating neighbors via 26-letter substitution — Time: O(wordListLen*26*L), Space: O(wordListLen*L)
import string
from collections import deque
from typing import List


class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        word_set = set(wordList)
        if endWord not in word_set:
            return 0

        q = deque([(beginWord, 1)])
        visited = {beginWord}
        while q:
            word, steps = q.popleft()
            if word == endWord:
                return steps
            for i in range(len(word)):
                for ch in string.ascii_lowercase:
                    if ch == word[i]:
                        continue
                    candidate = word[:i] + ch + word[i + 1:]
                    if candidate in word_set and candidate not in visited:
                        visited.add(candidate)
                        q.append((candidate, steps + 1))
        return 0


if __name__ == "__main__":
    sol = Solution()
    print("expected 5, got", sol.ladderLength("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"]))
    print("expected 0, got", sol.ladderLength("hit", "cog", ["hot", "dot", "dog", "lot", "log"]))
    print("expected 2, got", sol.ladderLength("a", "c", ["a", "b", "c"]))
