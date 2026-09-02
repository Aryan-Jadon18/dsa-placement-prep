# Bidirectional BFS — Time: O(26*L*wordListLen) with much smaller constant, Space: O(wordListLen*L)
import string
from typing import List, Set


class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        word_set = set(wordList)
        if endWord not in word_set:
            return 0
        if beginWord == endWord:
            return 1

        front: Set[str] = {beginWord}
        back: Set[str] = {endWord}
        visited = {beginWord, endWord}
        steps = 1
        L = len(beginWord)

        while front and back:
            # always expand the smaller frontier
            if len(front) > len(back):
                front, back = back, front

            next_front: Set[str] = set()
            for word in front:
                for i in range(L):
                    for ch in string.ascii_lowercase:
                        if ch == word[i]:
                            continue
                        candidate = word[:i] + ch + word[i + 1:]
                        if candidate in back:
                            return steps + 1
                        if candidate in word_set and candidate not in visited:
                            visited.add(candidate)
                            next_front.add(candidate)
            front = next_front
            steps += 1

        return 0


if __name__ == "__main__":
    sol = Solution()
    print("expected 5, got", sol.ladderLength("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"]))
    print("expected 0, got", sol.ladderLength("hit", "cog", ["hot", "dot", "dog", "lot", "log"]))
    print("expected 2, got", sol.ladderLength("a", "c", ["a", "b", "c"]))
