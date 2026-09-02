# BFS with O(wordListLen) neighbor scan per word — Time: O(wordListLen^2 * L), Space: O(wordListLen)
from collections import deque
from typing import List


class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        words = list(wordList)
        if endWord not in words:
            return 0

        def one_letter_diff(a: str, b: str) -> bool:
            diff = 0
            for ca, cb in zip(a, b):
                if ca != cb:
                    diff += 1
                    if diff > 1:
                        return False
            return diff == 1

        visited = {beginWord}
        q = deque([(beginWord, 1)])
        while q:
            word, steps = q.popleft()
            if word == endWord:
                return steps
            for candidate in words:
                if candidate not in visited and one_letter_diff(word, candidate):
                    visited.add(candidate)
                    q.append((candidate, steps + 1))
        return 0


if __name__ == "__main__":
    sol = Solution()
    print("expected 5, got", sol.ladderLength("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"]))
    print("expected 0, got", sol.ladderLength("hit", "cog", ["hot", "dot", "dog", "lot", "log"]))
    print("expected 2, got", sol.ladderLength("a", "c", ["a", "b", "c"]))
