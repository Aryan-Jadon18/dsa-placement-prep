# Adjacent-pairs graph + Kahn's algorithm (BFS topological sort) — Time: O(N*L + V+E), Space: O(V+E)
from collections import defaultdict, deque
from typing import List


class Solution:
    def alienOrder(self, words: List[str]) -> str:
        letters = set("".join(words))
        graph = defaultdict(set)
        indegree = {c: 0 for c in letters}

        for w1, w2 in zip(words, words[1:]):
            min_len = min(len(w1), len(w2))
            found_diff = False
            for k in range(min_len):
                if w1[k] != w2[k]:
                    if w2[k] not in graph[w1[k]]:
                        graph[w1[k]].add(w2[k])
                        indegree[w2[k]] += 1
                    found_diff = True
                    break
            if not found_diff and len(w1) > len(w2):
                return ""

        q = deque(c for c in letters if indegree[c] == 0)
        order = []
        while q:
            letter = q.popleft()
            order.append(letter)
            for nxt in graph[letter]:
                indegree[nxt] -= 1
                if indegree[nxt] == 0:
                    q.append(nxt)

        return "".join(order) if len(order) == len(letters) else ""


if __name__ == "__main__":
    sol = Solution()

    def is_valid(result, words):
        if not result:
            return False
        if set(result) != set("".join(words)) or len(result) != len(set(result)):
            return False
        pos = {c: i for i, c in enumerate(result)}
        for a, b in zip(words, words[1:]):
            min_len = min(len(a), len(b))
            diff = False
            for k in range(min_len):
                if a[k] != b[k]:
                    if pos[a[k]] > pos[b[k]]:
                        return False
                    diff = True
                    break
            if not diff and len(a) > len(b):
                return False
        return True

    r1 = sol.alienOrder(["wrt", "wrf", "er", "ett", "rftt"])
    print("got", r1, "valid:", is_valid(r1, ["wrt", "wrf", "er", "ett", "rftt"]))

    r2 = sol.alienOrder(["z", "x"])
    print("got", r2, "valid:", is_valid(r2, ["z", "x"]))

    r3 = sol.alienOrder(["abc", "ab"])
    print("expected '', got", repr(r3))
