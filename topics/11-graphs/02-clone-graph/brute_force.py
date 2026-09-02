# Two-pass BFS (clone nodes first, wire edges second) — Time: O(V+E), Space: O(V)
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

        # Pass 1: discover every original node, create empty clones
        mapping = {node: Node(node.val)}
        q = deque([node])
        while q:
            cur = q.popleft()
            for nei in cur.neighbors:
                if nei not in mapping:
                    mapping[nei] = Node(nei.val)
                    q.append(nei)

        # Pass 2: wire up neighbor lists on the clones
        for original, clone in mapping.items():
            clone.neighbors = [mapping[nei] for nei in original.neighbors]

        return mapping[node]


def build_graph(adj):
    """adj: {val: [neighbor_vals]} -> returns Node for val 1 (test helper)."""
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
