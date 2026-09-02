# DFS with memoization (clone-before-recurse breaks cycles) — Time: O(V+E), Space: O(V)
from collections import deque
from typing import Optional


class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


class Solution:
    def cloneGraph(self, node: Optional["Node"]) -> Optional["Node"]:
        if node is None:
            return None

        mapping = {}

        def dfs(n: "Node") -> "Node":
            if n in mapping:
                return mapping[n]
            clone = Node(n.val)
            mapping[n] = clone  # store BEFORE recursing to break cycles
            for nei in n.neighbors:
                clone.neighbors.append(dfs(nei))
            return clone

        return dfs(node)


def build_graph(adj):
    nodes = {v: Node(v) for v in adj}
    for v, neis in adj.items():
        nodes[v].neighbors = [nodes[n] for n in neis]
    return nodes[1] if nodes else None


def to_adj(node):
    if node is None:
        return {}
    seen = {}
    q = deque([node])
    seen[node.val] = node
    while q:
        cur = q.popleft()
        for nei in cur.neighbors:
            if nei.val not in seen:
                seen[nei.val] = nei
                q.append(nei)
    return {v: sorted(n.val for n in nd.neighbors) for v, nd in seen.items()}


if __name__ == "__main__":
    sol = Solution()
    g1 = build_graph({1: [2, 3], 2: [1, 3], 3: [1, 2]})
    clone1 = sol.cloneGraph(g1)
    print("expected {1: [2, 3], 2: [1, 3], 3: [1, 2]}, got", to_adj(clone1))
    assert clone1 is not g1

    g2 = build_graph({1: []})
    clone2 = sol.cloneGraph(g2)
    print("expected {1: []}, got", to_adj(clone2))

    print("expected None, got", sol.cloneGraph(None))
