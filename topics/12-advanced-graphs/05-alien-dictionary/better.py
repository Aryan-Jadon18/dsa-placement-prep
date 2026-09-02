# Adjacent-pairs graph + DFS postorder topological sort — Time: O(N*L + V+E), Space: O(V+E)
from collections import defaultdict
from typing import List

WHITE, GRAY, BLACK = 0, 1, 2


class Solution:
    def alienOrder(self, words: List[str]) -> str:
        letters = set("".join(words))
        graph = defaultdict(set)

        for w1, w2 in zip(words, words[1:]):
            min_len = min(len(w1), len(w2))
            found_diff = False
            for k in range(min_len):
                if w1[k] != w2[k]:
                    graph[w1[k]].add(w2[k])
                    found_diff = True
                    break
            if not found_diff and len(w1) > len(w2):
                return ""

        color = {c: WHITE for c in letters}
        postorder = []
        has_cycle = [False]

        def dfs(node: str) -> None:
            color[node] = GRAY
            for nxt in graph[node]:
                if color[nxt] == GRAY:
                    has_cycle[0] = True
                    return
                if color[nxt] == WHITE:
                    dfs(nxt)
                    if has_cycle[0]:
                        return
            color[node] = BLACK
            postorder.append(node)

        for letter in letters:
            if color[letter] == WHITE:
                dfs(letter)
            if has_cycle[0]:
                return ""

        return "".join(reversed(postorder))


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
